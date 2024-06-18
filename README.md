# Python Script Executor
- This service allows you to execute Python scripts securely within a controlled environment, supports umpy and pandas and other restricted available functions.
- Your Script must send the request body in this pattern `request body {"script": "def main(): ..."},`

### Using numpy and pandas
- numpy: Use import numpy as np
- pandas: Use import pandas as pd

### Curl Examples

```
curl --location 'https://scriptexecservice.pythonanywhere.com/execute' \
--header 'Content-Type: application/json' \
--data '{
    "script": "def main(): return {\"message\": \"Hello, World!\"}"
}'
```

```
numpy 

curl --location 'https://scriptexecservice.pythonanywhere.com/execute' \
--header 'Content-Type: application/json' \
--data '{
    "script": "def main():\r\n    arr = np.array([1, 2, 3, 4, 5])\r\n    sum_of_elements = int(np.sum(arr)) \r\n    mean_of_elements = float(np.mean(arr))\r\n    return {\r\n        \"array\": arr.tolist(), \r\n        \"sum\": sum_of_elements,\r\n        \"mean\": mean_of_elements\r\n    }"
}'

```

### Useful links
- https://www.pythonescaper.com/
- https://realpython.com/python-exec/