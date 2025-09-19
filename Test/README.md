# 🧐 教务系统研究
### 基本信息
- 教务系统**主网址**: **[https://jwjx.gxnu.edu.cn/](https://jwjx.gxnu.edu.cn)**
- 教务系统**主页面网址**： **[https://jwjx.gxnu.edu.cn/wfw/manager/](https://jwjx.gxnu.edu.cn/wfw/manager "https://jwjx.gxnu.edu.cn/wfw/manager")**

### 基本流程
1. 在请求教务系统的网址 **[https://jwjx.gxnu.edu.cn](https://jwjx.gxnu.edu.cn)** 之后，会试图**重定向跳转**到教务系统的主页面网址 **~/wfw/manger/**
2. 在由主网址重定向跳转到主页面网址之后，如果之前的**登录状态仍然有效**，会直接成功进入并渲染教务系统的主页面；如果**没有登录或者之前的登录状态失效**，接下来会跳转至 **SSO统一身份认证平台**，附带相关认证参数，比如：
    > https://sso.gxnu.edu.cn/cas/login?service=https://jwjx.gxnu.edu.cn/sso/login/3rd/432？referer=https%3A%2F%2Fjwjx.gxnu.edu.cn%2Fwfw%2Fmanage 
    
    > (似乎通常固定是这个 URL )

3. 之后再向**这个跳转而来的 SSO 认证 URL**，发送 **POST 请求**，其中附带的上传的**表单数据 Data **要求有：

	| 键（Key） | 值（Value） | 示例（Example） |
	| ------------ | ------------ | ------------ |
	| username | 用户输入的学号/工号 | 1234567 |
	| mobileCode | 不知道是什么，但是一般会有明文的密码在这里作为值 | impassword |
	| password | 密码，但是会使用RSA加密 | 7ad9acf73b012b25ffa3a9... |
	| authcode | 不知道， 一般为 “”， 即空白字符串 |   |
	| rememberMe | 对应页面上的是否 “记住我”，值一般为 “true” | true |
	| execution | CAS协议中的执行令牌，下文有详细分析 | 8099a4e8-2bda-43d2-a6... |
	| \_eventId | 通常为 “submit”，表示提交登录 | submit |

4. 在用POST方法**将正确的表单数据上传**之后，会跳转一个 URL，通常长这样：
    > https://jwjx.gxnu.edu.cn/sso/login/3rd/432?referer=https://jwjx.gxnu.edu.cn/wfw/manage&ticket=ST-1984093-0yN5whtdSWHA6QBzeAEc-zfsoft.com

    > 其中的 **ticket** 就是 **SSO 认证的票据**，通过 URL 参数传给教务系统，教务系统会验证，教务系统收到票据后，向CAS服务器验证票据有效性，验证通过后，教务系统创建用户会话，用户进入系统，即为**跳转到原来一开始教务系统请求验证跳转的SSO的网址（即第五步）：**  就是包含在 **referer** 中的 https://jwjx.gxnu.edu.cn/wfw/manage 这个网址

5. 教务系统**成功认证**后，会跳转回 URL https://jwjx.gxnu.edu.cn/wfw/manage 在浏览器中的表现为开始渲染教务系统的主页面，**完成登录**

### 参数分析

> 一些参数已经就是字面意思了，十分好理解，这里只进行部分复杂参数的分析

####  ***password*** 
- 密码，但是会使用RSA加密，其中会使用 **Modulus（RSA模数）** 和 **public_exponent （公钥指数）** 来作为参数来创建RSA密钥对
- 这个 **Modulus** 和 **public_exponent** 会从 URL [https://sso.gxnu.edu.cn/cas/v2/getPubKey](https://sso.gxnu.edu.cn/cas/v2/getPubKey) 的 **GET 请求** 中获取
- 在这个请求返回的响应内容就是 **modulus** 和 **exponent** 这两个键值对内容，其中的 **exponent** 似乎固定位 10001，这个 URL 貌似普通的 GET 请求就可以请求到，不需要什么 Cookies，Header 之类的貌似

#### ***execution***
- CAS协议中的 **执行令牌(Execution Token)** ，用于防止CSRF攻击
    ##### 由 **Base64** 解密之后的内容，由两部分组成：
  1. **UUID** 前缀，比如 644bb3a9-d289-40ad-ae36-bed672e86cc5_
  2. 长字符串：Base64 编码的 **JWT（JSON Web Token）** ，组成如下（原始数据为 Json 格式）：
      
     | 键（Key） | 值（Value）   | 示例（Example）                          |
     | -------- |------------|--------------------------------------|
     |alg| 加密算法       | HS256                                |
     |typ| 类型         | JWT                                  |
     |jti| JWT唯一标识符   | 6449c2d3-e2b5-40c4-b683-ed40f66645b0 |
     |sub| 主题（即用户学号）  | 2024xxxxx038                         |
     |authorities| 不清楚        | []                                   |
     |iss| 签发者（SSO系统） | https://sso.gxnu.edu.cn/cas          |
     |iat| 签发时间（时间戳）  | 1726189924                           |
     |exp| 过期时间 （时间戳） | 1726193524                                     |