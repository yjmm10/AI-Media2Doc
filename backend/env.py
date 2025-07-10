# -*- coding: UTF-8 -*-
import os
from dotenv import load_dotenv

# 自动加载 .env 文件
load_dotenv()

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3")
LLM_MODEL_ID = os.getenv("MODEL_ID")
LLM_API_KEY = os.getenv("ARK_API_KEY") or os.getenv("LLM_API_KEY")
TOS_ACCESS_KEY = os.getenv("TOS_ACCESS_KEY")
TOS_SECRET_KEY = os.getenv("TOS_SECRET_KEY")
TOS_ENDPOINT = os.getenv("TOS_ENDPOINT")
TOS_REGION = os.getenv("TOS_REGION")
TOS_BUCKET = os.getenv("TOS_BUCKET")
AUC_APP_ID = os.getenv("AUC_APP_ID")
AUC_ACCESS_TOKEN = os.getenv("AUC_ACCESS_TOKEN")
AUC_CLUSTER_ID = os.getenv("AUC_CLUSTER_ID", None)  # 选填, 填这个可以试用
WEB_ACCESS_PASSWORD = os.getenv("WEB_ACCESS_PASSWORD", None)  # 选填, 填这个可以开启 Web 端访问密码

# 环境变量验证
def validate_env_vars():
    """验证必需的环境变量是否已设置"""
    required_vars = {
        "LLM_MODEL_ID": LLM_MODEL_ID,
        "LLM_API_KEY": LLM_API_KEY,
        "TOS_ACCESS_KEY": TOS_ACCESS_KEY,
        "TOS_SECRET_KEY": TOS_SECRET_KEY,
        "TOS_ENDPOINT": TOS_ENDPOINT,
        "TOS_REGION": TOS_REGION,
        "TOS_BUCKET": TOS_BUCKET,
        "AUC_APP_ID": AUC_APP_ID,
        "AUC_ACCESS_TOKEN": AUC_ACCESS_TOKEN,
    }
    
    missing_vars = []
    for var_name, var_value in required_vars.items():
        if not var_value:
            missing_vars.append(var_name)
    
    if missing_vars:
        raise ValueError(f"缺少必需的环境变量: {', '.join(missing_vars)}")
    
    print("环境变量验证通过")

# 在模块加载时进行验证
try:
    validate_env_vars()
except ValueError as e:
    print(f"环境变量验证失败: {e}")
    print("请检查 variables.env 文件或环境变量设置")
