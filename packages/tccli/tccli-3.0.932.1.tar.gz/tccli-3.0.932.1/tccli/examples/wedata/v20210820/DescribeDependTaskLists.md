**Example 1: 通过taskIds查询task详情列表**

通过taskIds查询task详情列表

Input: 

```
tccli wedata DescribeDependTaskLists --cli-unfold-argument  \
    --TaskIds abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "abc",
                "VirtualTaskId": "abc",
                "VirtualFlag": true,
                "TaskName": "abc",
                "WorkflowId": "abc",
                "RealWorkflowId": "abc",
                "WorkflowName": "abc",
                "FolderId": "abc",
                "FolderName": "abc",
                "CreateTime": "abc",
                "LastUpdate": "abc",
                "Status": "abc",
                "InCharge": "abc",
                "InChargeId": "abc",
                "StartTime": "abc",
                "EndTime": "abc",
                "ExecutionStartTime": "abc",
                "ExecutionEndTime": "abc",
                "CycleType": "abc",
                "CycleStep": 1,
                "CrontabExpression": "abc",
                "DelayTime": 1,
                "StartupTime": 1,
                "RetryWait": 1,
                "RetryAble": 1,
                "TaskAction": "abc",
                "TryLimit": 1,
                "RunPriority": 1,
                "TaskType": {
                    "TypeDesc": "abc",
                    "TypeId": 0,
                    "TypeSort": "abc"
                },
                "BrokerIp": "abc",
                "ClusterId": "abc",
                "MinDateTime": "abc",
                "MaxDateTime": "abc",
                "ExecutionTTL": 0,
                "SelfDepend": "abc",
                "LeftCoordinate": 0,
                "TopCoordinate": 0,
                "Notes": "abc",
                "InstanceInitStrategy": "abc",
                "YarnQueue": "abc",
                "LastSchedulerCommitTime": "abc",
                "NormalizedJobStartTime": "abc",
                "SchedulerDesc": "abc",
                "ResourceGroup": "abc",
                "Creator": "abc",
                "DependencyRel": "abc",
                "DependencyWorkflow": "abc",
                "EventListenerConfig": "abc",
                "EventPublisherConfig": "abc",
                "VirtualTaskStatus": "abc",
                "TaskLinkInfo": {
                    "Id": "abc",
                    "LinkKey": "abc",
                    "TaskFrom": "abc",
                    "TaskTo": "abc",
                    "InCharge": "abc",
                    "LinkDependencyType": "abc",
                    "Offset": "abc",
                    "LinkType": "abc",
                    "WorkflowId": "abc"
                },
                "ProductName": "abc",
                "ProjectId": "abc",
                "ProjectIdent": "abc",
                "ProjectName": "abc",
                "OwnId": "abc",
                "UserId": "abc",
                "TenantId": "abc",
                "UpdateUser": "abc",
                "UpdateTime": "abc",
                "UpdateUserId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

