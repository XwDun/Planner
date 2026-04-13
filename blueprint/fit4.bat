python -c cmd "
import numpy as np
import pandas as pd
from io import StringIO

# 读取数据
df = pd.read_csv('fit_data.csv')
x = df['x'].values
y = df['y'].values

# 四次多项式拟合
coefs = np.polyfit(x, y, 4)

# 输出结果
print('=== 四次多项式拟合结果 ===')
print('拟合公式：y = a4·x⁴ + a3·x³ + a2·x² + a1·x + a0')
print('系数：')
print(f'a4 = {coefs[0]:.6f}')
print(f'a3 = {coefs[1]:.6f}')
print(f'a2 = {coefs[2]:.6f}')
print(f'a1 = {coefs[3]:.6f}')
print(f'a0 = {coefs[4]:.6f}')
print('\n完整拟合式：')
print(f'y = {coefs[0]:.4f}x⁴ + {coefs[1]:.4f}x³ + {coefs[2]:.4f}x² + {coefs[3]:.4f}x + {coefs[4]:.4f}') 
"