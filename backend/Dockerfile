FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/.venv/bin:$PATH"

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 复制应用代码
COPY . .

EXPOSE 8080

CMD ["python", "main.py"]
