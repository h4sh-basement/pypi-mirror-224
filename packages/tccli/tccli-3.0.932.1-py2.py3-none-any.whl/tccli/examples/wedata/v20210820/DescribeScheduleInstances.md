**Example 1: 测试**

测试

Input: 

```
tccli wedata DescribeScheduleInstances --cli-unfold-argument  \
    --SearchCondition.Instance.ExecutionSpace CYCLIC \
    --SearchCondition.Instance.ProductName DATA_DEV \
    --ProjectId 1460947878944567296 \
    --PageIndex 1 \
    --PageSize 3
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AvgCostTime": null,
                    "CostMillisecond": 0,
                    "CostTime": "00:00:00.000",
                    "CreateTime": "2023-03-15 15:15:42",
                    "CurRunDate": "2023-03-15 15:05:00",
                    "CycleType": "MINUTE_CYCLE",
                    "DependenceFulfillTime": null,
                    "DependencyRel": null,
                    "DoFlag": 2,
                    "EndTime": null,
                    "ErrorDesc": "该实例被手动终止",
                    "ExecutionSpace": "CYCLIC",
                    "FirstDependenceFulfillTime": null,
                    "FirstRunTime": "2023-01-16 11:00:00",
                    "FirstStartTime": null,
                    "FirstSubmitTime": "2023-01-16 11:23:38",
                    "FolderId": "22866126-84c3-11ed-8909-bc97e105ba60",
                    "FolderName": "qminliu",
                    "IgnoreEvent": false,
                    "InCharge": "qminliu",
                    "LastLog": "Had been kill",
                    "LastSchedulerDateTime": null,
                    "LastUpdate": "2023-03-15 15:22:58",
                    "MaxCostTime": null,
                    "MinCostTime": null,
                    "NextCurDate": "2023-03-15 15:10:00",
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": null,
                    "ProjectName": null,
                    "RedoFlag": 0,
                    "ResourceGroup": "20221229154930684210",
                    "ResourceInstanceId": "any",
                    "RunPriority": 6,
                    "RuntimeBroker": null,
                    "SchedulerDateTime": "2023-03-15 15:05:00",
                    "SchedulerDesc": null,
                    "SonList": null,
                    "StartTime": null,
                    "State": "EXPIRED",
                    "TaskId": "20230101114142907",
                    "TaskName": "retry_hive",
                    "TaskType": {
                        "TypeDesc": "Hive SQL",
                        "TypeId": 34,
                        "TypeSort": "数据计算"
                    },
                    "TenantId": "1315051789",
                    "Tries": 0,
                    "TryLimit": 5,
                    "VirtualFlag": null,
                    "WorkflowId": "332e31f8-84c3-11ed-8909-bc97e105ba60",
                    "WorkflowName": "up",
                    "YarnQueue": "root.dev"
                },
                {
                    "AvgCostTime": null,
                    "CostMillisecond": 0,
                    "CostTime": "00:00:00.000",
                    "CreateTime": "2023-03-15 15:15:40",
                    "CurRunDate": "2023-03-15 15:00:00",
                    "CycleType": "MINUTE_CYCLE",
                    "DependenceFulfillTime": null,
                    "DependencyRel": null,
                    "DoFlag": 2,
                    "EndTime": null,
                    "ErrorDesc": "该实例被手动终止",
                    "ExecutionSpace": "CYCLIC",
                    "FirstDependenceFulfillTime": null,
                    "FirstRunTime": "2023-01-16 11:00:00",
                    "FirstStartTime": null,
                    "FirstSubmitTime": "2023-01-16 11:23:38",
                    "FolderId": "22866126-84c3-11ed-8909-bc97e105ba60",
                    "FolderName": "qminliu",
                    "IgnoreEvent": false,
                    "InCharge": "qminliu",
                    "LastLog": "Had been kill",
                    "LastSchedulerDateTime": null,
                    "LastUpdate": "2023-03-15 15:22:58",
                    "MaxCostTime": null,
                    "MinCostTime": null,
                    "NextCurDate": "2023-03-15 15:05:00",
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": null,
                    "ProjectName": null,
                    "RedoFlag": 0,
                    "ResourceGroup": "20221229154930684210",
                    "ResourceInstanceId": "any",
                    "RunPriority": 6,
                    "RuntimeBroker": null,
                    "SchedulerDateTime": "2023-03-15 15:00:00",
                    "SchedulerDesc": null,
                    "SonList": null,
                    "StartTime": null,
                    "State": "EXPIRED",
                    "TaskId": "20230101114142907",
                    "TaskName": "retry_hive",
                    "TaskType": {
                        "TypeDesc": "Hive SQL",
                        "TypeId": 34,
                        "TypeSort": "数据计算"
                    },
                    "TenantId": "1315051789",
                    "Tries": 0,
                    "TryLimit": 5,
                    "VirtualFlag": null,
                    "WorkflowId": "332e31f8-84c3-11ed-8909-bc97e105ba60",
                    "WorkflowName": "up",
                    "YarnQueue": "root.dev"
                },
                {
                    "AvgCostTime": null,
                    "CostMillisecond": 0,
                    "CostTime": "00:00:00.000",
                    "CreateTime": "2023-03-15 15:15:38",
                    "CurRunDate": "2023-03-15 14:55:00",
                    "CycleType": "MINUTE_CYCLE",
                    "DependenceFulfillTime": null,
                    "DependencyRel": null,
                    "DoFlag": 2,
                    "EndTime": null,
                    "ErrorDesc": "该实例被手动终止",
                    "ExecutionSpace": "CYCLIC",
                    "FirstDependenceFulfillTime": null,
                    "FirstRunTime": "2023-01-16 11:00:00",
                    "FirstStartTime": null,
                    "FirstSubmitTime": "2023-01-16 11:23:38",
                    "FolderId": "22866126-84c3-11ed-8909-bc97e105ba60",
                    "FolderName": "qminliu",
                    "IgnoreEvent": false,
                    "InCharge": "qminliu",
                    "LastLog": "Had been kill",
                    "LastSchedulerDateTime": null,
                    "LastUpdate": "2023-03-15 15:22:58",
                    "MaxCostTime": null,
                    "MinCostTime": null,
                    "NextCurDate": "2023-03-15 15:00:00",
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": null,
                    "ProjectName": null,
                    "RedoFlag": 0,
                    "ResourceGroup": "20221229154930684210",
                    "ResourceInstanceId": "any",
                    "RunPriority": 6,
                    "RuntimeBroker": null,
                    "SchedulerDateTime": "2023-03-15 14:55:00",
                    "SchedulerDesc": null,
                    "SonList": null,
                    "StartTime": null,
                    "State": "EXPIRED",
                    "TaskId": "20230101114142907",
                    "TaskName": "retry_hive",
                    "TaskType": {
                        "TypeDesc": "Hive SQL",
                        "TypeId": 34,
                        "TypeSort": "数据计算"
                    },
                    "TenantId": "1315051789",
                    "Tries": 0,
                    "TryLimit": 5,
                    "VirtualFlag": null,
                    "WorkflowId": "332e31f8-84c3-11ed-8909-bc97e105ba60",
                    "WorkflowName": "up",
                    "YarnQueue": "root.dev"
                }
            ],
            "PageCount": 3,
            "PageNumber": 1,
            "PageSize": 3,
            "TotalCount": 876,
            "TotalPage": 292
        },
        "RequestId": "20805432-23c1-4c0c-9ae1-a622522034d1"
    }
}
```

