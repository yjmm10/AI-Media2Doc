ARG NODE_VERSION=22

FROM node:${NODE_VERSION}-slim

ENV NODE_ENV=development

WORKDIR /app

# 增加文件监视器限制以解决ENOSPC错误
RUN echo fs.inotify.max_user_watches=524288 | tee -a /etc/sysctl.conf

# 复制package文件以利用Docker缓存
COPY package*.json ./

# 安装依赖
RUN npm install

# 复制源代码
COPY . .

# 暴露端口
EXPOSE 5173

# 启动开发服务器
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
