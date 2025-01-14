#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 模块重写脚本

import os, json
import subprocess
from ruamel import yaml
from tdf_tool.tools.cli.bean.deps_item import DepsAnalysisUtil, DepsRecord
from tdf_tool.tools.cli.utils.yaml_utils import YamlFileUtils
from tdf_tool.tools.dependencies_analysis import DependencyAnalysis
from tdf_tool.tools.print import Print
from tdf_tool.tools.module.module_tools import ModuleTools
from tdf_tool.tools.shell_dir import ShellDir


class ModuleDependenciesRewriteUtil:
    def __init__(self):
        Print.debug("开始进行依赖重写")
        self.moduleJsonData = ModuleTools.getModuleJsonData()
        self.moduleNameList = ModuleTools.getModuleNameList()
        self.initJsonData = ModuleTools.getInitJsonData()

    # 分析lock文件，获取所有的packages
    def _analysisLock(self):
        os.chdir(self.__moduleGenPath)
        # 分析前先执行pub upgrade
        os.popen("flutter pub upgrade").read()

        # 读取lock内容
        with open("pubspec.lock", encoding="utf-8") as f:
            doc = yaml.round_trip_load(f)
            if isinstance(doc, dict) and doc.__contains__("packages"):
                f.close()
                return doc["packages"]

    # 是否是壳模块
    def _isShellModule(self):
        return self.moduleJsonData[self.__moduleName]["type"] == "app"

    # 确认哪些依赖需要重写
    def _confirmRewriteDependencies(self, isShell):
        if isShell:  # 壳模块重写所有配置的依赖
            for item in self.moduleNameList:
                if item != self.__moduleName:  # 壳自己不加入重写列表
                    self.__needRewriteDependencies.append(item)
        else:  # 如果不是壳模块，则进行lock文件内的package列表和开发模块匹配，匹配上则添加到override列表
            for package in self.__moduleDependenciesMap:
                for module in self.moduleNameList:
                    if package == module:
                        self.__needRewriteDependencies.append(module)

        Print.stage("{0}中以下依赖将被override".format(self.__moduleName))
        Print.debug(self.__needRewriteDependencies)

    def _addOverrideDependencies(self):
        mDict = dict()
        for item in self.__needRewriteDependencies:
            mDict[item] = {"path": "../{0}/".format(item)}

        return mDict

    # 添加dependency_overrides

    def _rewriteDependencies(self, isShell):
        os.chdir(self.__moduleGenPath)
        with open("pubspec.yaml", encoding="utf-8") as f:
            doc = yaml.round_trip_load(f)
            if isinstance(doc, dict):
                self._confirmRewriteDependencies(isShell)
                if (
                    doc.__contains__("dependency_overrides")
                    and doc["dependency_overrides"] is not None
                ):
                    doc["dependency_overrides"] = None

                # 重写依赖
                overrideDict = dict()
                for item in self.__needRewriteDependencies:
                    if isShell:
                        overrideDict[item] = {
                            "path": "../.tdf_flutter/{0}/".format(item)
                        }
                    else:
                        overrideDict[item] = {"path": "../{0}/".format(item)}
                if len(self.__needRewriteDependencies) > 0:
                    doc["dependency_overrides"] = overrideDict

                with open("pubspec.yaml", "w+", encoding="utf-8") as reW:
                    yaml.round_trip_dump(
                        doc,
                        reW,
                        default_flow_style=False,
                        encoding="utf-8",
                        allow_unicode=True,
                    )
                    reW.close()
                    # 依赖重写完，执行pub upgrade更新lock文件
                    os.popen("flutter pub upgrade").read()
                    Print.debug("lock文件已更新")
            f.close()

    # 添加dependency_overrides，如果已存在模块的override，则不修改

    def _rewriteDependenciesIfUpdate(self, isShell):
        os.chdir(self.__moduleGenPath)
        with open("pubspec.yaml", encoding="utf-8") as f:
            doc = yaml.round_trip_load(f)
            if isinstance(doc, dict):
                self._confirmRewriteDependencies(isShell)

                global existUpdate
                existUpdate = False

                # 删除不存在于重写依赖列表中的key
                if (
                    doc.__contains__("dependency_overrides")
                    and doc["dependency_overrides"] is not None
                    and isinstance(doc["dependency_overrides"], dict)
                ):
                    keyList = list(doc["dependency_overrides"].keys())
                    for item in keyList:
                        if item not in self.__needRewriteDependencies:
                            Print.debug("${0}依赖被删除".format(item))
                            existUpdate = True
                            del doc["dependency_overrides"][item]

                if doc.__contains__("dependency_overrides"):
                    overrideDict = doc["dependency_overrides"]
                    if overrideDict is None:
                        overrideDict = dict()
                else:
                    overrideDict = dict()
                for item in self.__needRewriteDependencies:
                    if (
                        doc.__contains__("dependency_overrides")
                        and doc["dependency_overrides"] is not None
                        and isinstance(doc["dependency_overrides"], dict)
                        and doc["dependency_overrides"].get(item, -1) != -1
                    ):
                        Print.debug("${0}依赖已存在（不予修改）".format(item))
                    else:
                        Print.debug("${0}依赖不存在（添加）".format(item))
                        existUpdate = True
                        if isShell:
                            overrideDict[item] = {
                                "path": "../.tdf_flutter/{0}/".format(item)
                            }
                        else:
                            overrideDict[item] = {
                                "path": "../{0}/".format(item)}
                doc["dependency_overrides"] = overrideDict
                if existUpdate:
                    with open("pubspec.yaml", "w+", encoding="utf-8") as reW:
                        yaml.round_trip_dump(
                            doc,
                            reW,
                            default_flow_style=False,
                            encoding="utf-8",
                            allow_unicode=True,
                        )
                        reW.close()
                        # 依赖重写完，执行pub upgrade更新lock文件
                        os.popen("flutter pub upgrade").read()
                        Print.debug("lock文件已更新")
                else:
                    Print.debug("yaml无更新")

            f.close()

    # 重写依赖 本地依赖

    def rewrite(self, reWriteOnlyChange=False):
        ShellDir.goInShellDir()
        # 壳在生成package_config.json后，执行deps --json获取依赖树
        os.system('flutter pub upgrade')
        # 重写壳
        Print.step("在壳中重写所有模块")
        self._writeNewDeps("./", self.moduleNameList)
        shellPackageConfigJson = json.loads(os.popen('flutter pub deps --json').read())
        print(shellPackageConfigJson['root'])

        depsRecordList: list[DepsRecord] = []

        for module in self.moduleNameList:
            Print.step("{0}依赖分析...".format(module))
            record = DepsRecord(module)
            for packageItem in  shellPackageConfigJson['packages']:
                if packageItem['name'] == module:
                    moduleDeps: list[str] = packageItem['dependencies']
                    for depsItemName in moduleDeps:
                        if depsItemName in self.moduleNameList:
                            record.addDepsItemName(depsItemName)
            depsRecordList.append(record)
        
        depsUtils = DepsAnalysisUtil(depsRecordList)
       
        depsSortedList = depsUtils.analysis()

        for module in depsSortedList:
            Print.step("更新" + module)
            _modulePath = "../.tdf_flutter/" + module
            _record: list[DepsRecord]  = [record for record in depsRecordList if record.moduleName == module]
            self._writeNewDeps(_modulePath, _record[0].deps, False)
    
        # 重写壳
        Print.step("更新壳")
        self._writeNewDeps("./", self.moduleNameList)
        

    def _writeNewDeps(self, modulePath: str, deps: list[str], isShell: bool = True):
        yamlFileUtils = YamlFileUtils(modulePath)
        depsKeys = yamlFileUtils.readOverrideDepsKeys()

        isYamlOverrideSame = sorted(depsKeys) == sorted(deps)
        isLockAndYamlOverrideSame = self.validate_lock_and_yaml_file(modulePath, depsKeys)

        # 重写的依赖不一致，则需要重写并执行pub upgrade
        if isYamlOverrideSame and isLockAndYamlOverrideSame:
            Print.debug("yaml无变动，且已执行过flutter pub upgrade命令")
        else:
            if isYamlOverrideSame is not True:
                Print.debug("yaml文件有更新，执行upgrade")
            
            if isLockAndYamlOverrideSame is not True:
                Print.debug("lock文件或package_config.json文件不存在，执行upgrade")

            yamlFileUtils.writeOverrideDeps(deps, isShell=isShell)
            # 依赖重写完，执行pub upgrade更新lock文件
            command = "flutter pub upgrade"
            result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=modulePath)
            print("Standard Output:", result.stdout)
            Print.debug("lock文件已更新")
    
    # 是否执行过flutter pub upgrade（判断条件为是否存在lock文件和package_config.json文件）
    # def existDepsResult(self, modulePath) -> bool:
    #     packageConfigFilePath = os.path.join(modulePath, ".dart_tool/package_config.json")
    #     lockFilePath = os.path.join(modulePath, "pubspec.lock")
    #     return os.path.isfile(packageConfigFilePath) and os.path.isfile(lockFilePath)
    
    # 校验yaml中override的库，是否已在lock文件中存在且是相对路径源码引用
    def validate_lock_and_yaml_file(self, modulePath: str, depsKeys: list[str]) -> bool:
        lockPath = os.path.join(modulePath, "pubspec.lock")
        pathPackages: list = []
        with open(lockPath, "r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            packages: dict = data['packages']
            for item in packages.keys():
                if packages[item]['source'] == 'path':
                    pathPackages.append(item)

        # 两者的lock文件内override的库一致，则不需要重新执行upgrade
        return sorted(depsKeys) == sorted(pathPackages)
        

