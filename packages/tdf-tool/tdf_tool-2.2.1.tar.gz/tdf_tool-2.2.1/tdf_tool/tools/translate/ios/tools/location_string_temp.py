class LocationStringTempClass:
    class_h = r"""
//************************************************************
//
//  代码千万行，规范第一条；编码不规范，队友两行泪！
//
//  Created by pangtouyu on 2022/5/24.
//  
//
// @class TDFLocationStringTempClass
// @abstract 字符串本地化的类，脚本自动生成，不能手动修改
// @discussion 字符串本地化的类，脚本自动生成，不能手动修改
//

#import <Foundation/Foundation.h>

#define TDFLocationStringTempDefine(key, comment) \
        [TDFLocationStringTempClass stringFormStings:(key)]


@interface TDFLocationStringTempClass : NSObject
+ (NSString *)stringFormStings:(NSString *)key;
@end

    """

    class_m = r"""
//
//  TDFLocationStringTempClass.m
//  Test
//
//************************************************************
//*                                                          *
//*            _______     ______         ______             *
//*           |__   __|    |  __ \       / ____/             *
//*             /  /       | (__) |     / /__                *
//*            /__/        |_____/     /_/                   *
//*                                                          *
//*                                                          *
//************************************************************
//
//  代码千万行，规范第一条；编码不规范，队友两行泪！
//
//  Created by pangtouyu on 2022/5/24.
//  
//
// @class TDFLocationStringTempClass
//

#import "TDFLocationStringTempClass.h"
#import <TDFInternationalKit/NSBundle+Language.h>

@implementation TDFLocationStringTempClass

+ (NSString *)stringFormStings:(NSString *)key {
    
    NSString * LocalizableBundlePath = [[NSBundle bundleForClass:NSClassFromString(@"TDFLocationStringTempClass")].resourcePath stringByAppendingString:@"/TDFLocationStringTempBundle.bundle"];
    
    NSString *language = [NSBundle currentLanguage];
    
   
    NSString *path = [[NSBundle bundleWithPath:LocalizableBundlePath] pathForResource:language ofType:@"lproj"];
    NSBundle * LocalizableBundle = [NSBundle bundleWithPath:path] ?:  [NSBundle mainBundle];
    NSString *localizedString = [LocalizableBundle localizedStringForKey:key value:nil table:@"TDFLocationStringTempTable"];

    return localizedString;
}

@end

    """
