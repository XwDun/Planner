# 轻量基础镜像
FROM ubuntu:noble

# 非交互安装环境
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# 基础系统工具
RUN apt update && apt install -y --no-install-recommends \
    wget curl git ca-certificates \
    libx11-6 libxt6 libgl1 \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------
# Python 3.14 安装
# ------------------------------
RUN apt update && apt install -y --no-install-recommends \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/nightly \
    && apt update && apt install -y \
    python3.14 python3.14-dev python3.14-distutils \
    && rm -rf /var/lib/apt/lists/*

# 安装 pip
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.14

# 工作目录
WORKDIR /app

# 复制依赖清单
COPY requirements.txt .

# 从 requirements 安装 Python 科学计算包
RUN python3.14 -m pip install --no-cache-dir -r requirements.txt

# ------------------------------
# 安装 Wolfram Engine (Mathematica)
# ------------------------------
RUN wget -q https://account.wolfram.com/ark/downloads/WolframEngine/14.1/Linux -O wolfram-install.sh \
    && chmod +x wolfram-install.sh \
    && ./wolfram-install.sh --auto \
    && rm -f wolfram-install.sh

# ------------------------------
# MATLAB 运行依赖（最小化）
# ------------------------------
RUN apt update && apt install -y --no-install-recommends \
    libgtk2.0-0 libxcursor1 libxrandr2 libxi6 \
    libxcomposite1 libxdamage1 libxtst6 \
    libasound2 libpulse0 libnss3 libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------
# Lean 4 + mathlib4
# ------------------------------
RUN curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
ENV PATH="/root/.elan/bin:$PATH"

RUN lake +leanprover-community/mathlib4 default && \
    echo "Lean 4 and mathlib4 installed"

# ------------------------------
# 清理
# ------------------------------
RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# 默认启动
CMD ["/bin/bash"]