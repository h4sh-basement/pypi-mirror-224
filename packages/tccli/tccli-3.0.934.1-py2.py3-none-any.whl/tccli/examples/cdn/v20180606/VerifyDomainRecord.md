**Example 1: 验证解析记录-2**

正常回包

Input: 

```
tccli cdn VerifyDomainRecord --cli-unfold-argument  \
    --Domain www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "b6926bb2-d0b5-42bc-b17f-e4402bdb9e9b",
        "Result": true
    }
}
```

**Example 2: 验证解析记录**

异常返回

Input: 

```
tccli cdn VerifyDomainRecord --cli-unfold-argument  \
    --Domain www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "2424"
    }
}
```

