**Example 1: 通用票据识别（高级版）**

通用票据识别（高级版）识别多张票据

Input: 

```
tccli ocr RecognizeGeneralInvoice --cli-unfold-argument  \
    --ImageUrl abc \
    --EnableMultiplePage True
```

Output: 
```
{
    "Response": {
        "MixedInvoiceItems": [
            {
                "Code": "OK",
                "Type": 3,
                "SubType": "VatSpecialInvoice",
                "TypeDescription": "增值税发票",
                "SubTypeDescription": "增值税专用发票",
                "Polygon": {
                    "LeftBottom": {
                        "X": -18,
                        "Y": 880
                    },
                    "LeftTop": {
                        "X": -18,
                        "Y": 34
                    },
                    "RightBottom": {
                        "X": 1381,
                        "Y": 880
                    },
                    "RightTop": {
                        "X": 1381,
                        "Y": 34
                    }
                },
                "Angle": 270,
                "SingleInvoiceInfos": {
                    "AirTransport": null,
                    "BusInvoice": null,
                    "MachinePrintedInvoice": null,
                    "MotorVehicleSaleInvoice": null,
                    "NonTaxIncomeElectronicBill": null,
                    "NonTaxIncomeGeneralBill": null,
                    "OtherInvoice": null,
                    "QuotaInvoice": null,
                    "ShippingInvoice": null,
                    "TaxiTicket": null,
                    "TollInvoice": null,
                    "TrainTicket": null,
                    "UsedCarPurchaseInvoice": null,
                    "VatCommonInvoice": null,
                    "VatElectronicCommonInvoice": null,
                    "VatElectronicInvoiceBlockchain": null,
                    "VatElectronicInvoiceFull": null,
                    "VatElectronicInvoiceToll": null,
                    "VatElectronicSpecialInvoice": null,
                    "VatElectronicSpecialInvoiceFull": null,
                    "VatInvoiceRoll": null,
                    "VatSpecialInvoice": {
                        "AgentMark": 0,
                        "Buyer": "深圳市腾讯计算机系统有限公司",
                        "BuyerAddrTel": "深圳市南山区高新区高新南一路飞亚达大厦5-10楼0755-86013388",
                        "BuyerBankAccount": "招商银行深圳分行振兴支行817282299619961",
                        "BuyerTaxID": "440300708461136",
                        "CheckCode": "",
                        "Ciphertext": "*7-0<84019---5+68315-99->/51,>814<1/7922/<-23/908+>7474+3,78312-072<3<729-+4<6*315-094,->/5>18493/1-60*6-43/90<--78",
                        "City": "深圳市",
                        "Code": "4403152130",
                        "CodeConfirm": "4403152130",
                        "CompanySealContent": "深圳市游戏科技有限公司,04000,发票专用章,N",
                        "CompanySealMark": 1,
                        "Date": "2016年04月11日",
                        "ElectronicFullMark": 0,
                        "ElectronicFullNumber": "",
                        "FormName": "发票联",
                        "FormType": "三",
                        "Issuer": "张三",
                        "Kind": "服务",
                        "MachineCode": "",
                        "Number": "14998456",
                        "NumberConfirm": "14998456",
                        "OilMark": 0,
                        "PretaxAmount": "778.44",
                        "Province": "广东省",
                        "QRCodeMark": 0,
                        "Receiptor": "李明",
                        "Remark": "",
                        "Reviewer": "晓艾",
                        "Seller": "深圳市游戏科技有限公司",
                        "SellerAddrTel": "深圳市南山区高新南一道3号赋安科技大楼A座301室0755-86315454",
                        "SellerBankAccount": "浦发行深圳科技园支行79210154740015474",
                        "SellerTaxID": "440300094040109",
                        "ServiceName": "",
                        "Tax": "46.71",
                        "TaxSealContent": "",
                        "Title": "深圳增值税专用发票",
                        "Total": "825.15",
                        "TotalCn": "捌佰贰拾伍圆壹角伍分",
                        "TransitMark": 0,
                        "TravelTax": "",
                        "BlockChainMark": 0,
                        "AcquisitionMark": 0,
                        "VatInvoiceItemInfos": [
                            {
                                "DateEnd": "",
                                "DateStart": "",
                                "LicensePlate": "",
                                "Name": "技术服务费",
                                "Price": "",
                                "Quantity": "",
                                "Specification": "",
                                "Tax": "46.71",
                                "TaxRate": "6%",
                                "Total": "778.44",
                                "Unit": "",
                                "VehicleType": ""
                            }
                        ]
                    }
                },
                "Page": 1,
                "CutImage": ""
            },
            {
                "Code": "OK",
                "Type": 13,
                "SubType": "TollInvoice",
                "TypeDescription": "过路过桥费发票",
                "SubTypeDescription": "过路过桥费发票",
                "Polygon": {
                    "LeftBottom": {
                        "X": 30,
                        "Y": 1478
                    },
                    "LeftTop": {
                        "X": 30,
                        "Y": 886
                    },
                    "RightBottom": {
                        "X": 496,
                        "Y": 1478
                    },
                    "RightTop": {
                        "X": 496,
                        "Y": 886
                    }
                },
                "Angle": 0.11452838033437729,
                "SingleInvoiceInfos": {
                    "AirTransport": null,
                    "BusInvoice": null,
                    "MachinePrintedInvoice": null,
                    "MotorVehicleSaleInvoice": null,
                    "NonTaxIncomeElectronicBill": null,
                    "NonTaxIncomeGeneralBill": null,
                    "OtherInvoice": null,
                    "QuotaInvoice": null,
                    "ShippingInvoice": null,
                    "TaxiTicket": null,
                    "TollInvoice": {
                        "Code": "144031700221",
                        "Date": "2018年08月07日",
                        "Entrance": "前海",
                        "Exit": "大铲湾",
                        "HighwayMark": 1,
                        "Kind": "交通",
                        "Number": "27357827",
                        "QRCodeMark": 0,
                        "Time": "06:14:03",
                        "Title": "深圳市广深沿江高速公路投资有限公司通用机打发票",
                        "Total": "5.00"
                    },
                    "TrainTicket": null,
                    "UsedCarPurchaseInvoice": null,
                    "VatCommonInvoice": null,
                    "VatElectronicCommonInvoice": null,
                    "VatElectronicInvoiceBlockchain": null,
                    "VatElectronicInvoiceFull": null,
                    "VatElectronicInvoiceToll": null,
                    "VatElectronicSpecialInvoice": null,
                    "VatElectronicSpecialInvoiceFull": null,
                    "VatInvoiceRoll": null,
                    "VatSpecialInvoice": null
                },
                "Page": 1,
                "CutImage": ""
            },
            {
                "Code": "OK",
                "Type": 2,
                "SubType": "TrainTicket",
                "TypeDescription": "火车票",
                "SubTypeDescription": "火车票",
                "Polygon": {
                    "LeftBottom": {
                        "X": 517,
                        "Y": 1229
                    },
                    "LeftTop": {
                        "X": 517,
                        "Y": 950
                    },
                    "RightBottom": {
                        "X": 963,
                        "Y": 1229
                    },
                    "RightTop": {
                        "X": 963,
                        "Y": 950
                    }
                },
                "Angle": 0.04854407534003258,
                "SingleInvoiceInfos": {
                    "AirTransport": null,
                    "BusInvoice": null,
                    "MachinePrintedInvoice": null,
                    "MotorVehicleSaleInvoice": null,
                    "NonTaxIncomeElectronicBill": null,
                    "NonTaxIncomeGeneralBill": null,
                    "OtherInvoice": null,
                    "QuotaInvoice": null,
                    "ShippingInvoice": null,
                    "TaxiTicket": null,
                    "TollInvoice": null,
                    "TrainTicket": {
                        "AdditionalFare": "",
                        "DateGetOn": "2018年03月06日",
                        "GateNumber": "",
                        "HandlingFee": "",
                        "Kind": "交通",
                        "Name": "周周",
                        "Number": "Z96X089517",
                        "OriginalFare": "",
                        "PickUpAddress": "上海自",
                        "QRCodeMark": 0,
                        "ReceiptNumber": "",
                        "ReimburseOnlyMark": 0,
                        "Seat": "新空调硬座",
                        "SeatNumber": "02车016号",
                        "SerialNumber": "30671300960307X089517",
                        "StationGetOff": "南京",
                        "StationGetOn": "上海",
                        "TicketChange": "0",
                        "TimeGetOn": "18:51",
                        "Title": "",
                        "Total": "46.50",
                        "TotalCn": "",
                        "TrainNumber": "Z196",
                        "UserID": "3210231991****6666"
                    },
                    "UsedCarPurchaseInvoice": null,
                    "VatCommonInvoice": null,
                    "VatElectronicCommonInvoice": null,
                    "VatElectronicInvoiceBlockchain": null,
                    "VatElectronicInvoiceFull": null,
                    "VatElectronicInvoiceToll": null,
                    "VatElectronicSpecialInvoice": null,
                    "VatElectronicSpecialInvoiceFull": null,
                    "VatInvoiceRoll": null,
                    "VatSpecialInvoice": null
                },
                "Page": 1,
                "CutImage": ""
            }
        ],
        "RequestId": "4f181ebb-ff56-4e66-b3b1-a45bd7ec233e",
        "TotalPDFCount": 1
    }
}
```

