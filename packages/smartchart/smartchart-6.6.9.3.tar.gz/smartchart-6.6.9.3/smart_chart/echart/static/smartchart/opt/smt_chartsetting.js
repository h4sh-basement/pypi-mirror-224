function smt_chartsetting(zj){
    let c;
    if(zj==='数据处理'){c=`let dataset = __dataset__; //传入dataset
let legend_label = ds_rowname(dataset); //自动获取legend
let xlabel = dataset[0].slice(1); //x轴的标签列
dataset = ds_createMap(dataset); //转化成字典
//处理字典
let series =[];
for (let i=0;i< legend_label.length;i++){
    series.push({type:'bar',data:dataset[legend_label[i]]});
}
//处理数组
for (let i=1;i< dataset[0].length;i++){
    series.push({type: 'line'})
}
#图形中可用转化函数
##数据集转化
ds_transform(dataset)  行列转置   
ds_createMap(dataset)  将数组生成结果表示为key->[], 常用于echarts指定数据  
ds_createMap_all(dataset)  将二维数组转成字典[{A:A1,B:B1,C:C1},...], 常用于饼图  
ds_mapToList(dataset)  将字典还原成二维数组, 常用于将nosql(mongodb,es..)数据源数据处理   
ds_pivot(dataset) 将二维数组(维度,维度,值)的第二列的维度透视为行   
ds_distinct(dataset)   对单个或多个二维数组去重   
ds_filter(dataset, fun)   fun为函数如: item=>item[0]=='顺德' 
ds_sort(dataset, index=0, asc=true)按照列序号排序,默认升序,index参数可以是函数,如(a,b)=>a.qty - b.qty
ds_remove_column(dataset,remove_list=[0])  默认移除第一列, 也要移除指定的多个列  
ds_split(data,sep=',',head_add=[])  将第一列拆分成多个字段,默认逗号分隔, 如果不传表头,取SQL中的字段名拆分  

##数据集关联
ds_leftjoin(a,b)  按照第一列左关联两个数据集   
ds_crossjoin(a,b)     
ds_fulljoin(a,b)     
ds_union(a,b) 合并两个数据集,取第一个数据集的表头   

##数据集刷新
ds_param(name)  传入参数名,获取图形点击时传递来的参数值   
ds_setParam('参数名', 参数值)  设定全局参数, 此方法将自动判断当参数值为空时, 删除参数回到初始未传参状态   
ds_refresh(id, param=filter_param)  刷新图形, id为图形序号,默认采取全局参数刷新,也可指定param,参数为字典{"参数名":"值",...}  

##数据处理
ds_rowname(dataset,start_row=1,column=0)  获取指定列的数据, 常用于获取维度   
ds_toThousands(num)  转逗号分隔的千分位  
ds_round(num,qty=2)  小数点处理, 默认保留两位小数   

##Excel数据集
ds_excel_refresh(dataset)  刷新复杂报表, dataset格式:{df0:二维数组, df1:二维数组,..}  
ds_excel_value(fillCells,clear=false)  指定单元格获取复杂报表中的数据, fillcells格式:['A1','B2'],一般用于数据填报  

##数据上传下载
ds_save(seq, contents) 保存数据
ds_download(name, dataset) 下载数据
ds_uploadfile(file, filename, callback=null)  上传文件  

//处理prometheus
let df = __dataset__;
let result = df.data.result;
let dataset = [['instance','state','qty']];
for(let item of result){
    let pmetric = item.metric;
    let pvalue = item.value;
    dataset.push([pmetric.instance,pmetric.state,pvalue[1]]);
}
dataset = ds_pivot(dataset);
`}
    else if(zj ==='颜色背景'){c=`//指定背景颜色
backgroundColor: '#3bd482',
//指定图列的顺序颜色
color : ['#b3c7bc','#cdd6bc','#d4713b'],
//定义画布位置
grid:{
    top: '5px',
    bottom: '5px',
    left: '5px',
    right: '5px',
}
`}
    else if(zj ==='图形标题'){c=`title: {
    text: "更多配置说明",//图的标题
    link: "smartchart.cn",//主标题文本超链接
    subtext: "", //副标题文本，
    sublink: "",//副标题文本超链接
    x: "", //水平坐标，默认为左侧center|left|right| {number}（px)
    y: "", //top|bottom|center|{number}（y坐标，单位px）
    backgroundColor: 'rgba(0,0,0,0)',
    borderColor: '#ccc',       // 标题边框颜色
    borderWidth: 0,            // 标题边框线宽，单位px，默认为0（无边框）
    padding: 5,                // 标题内边距，单位px，默认各方向内边距为5，
    itemGap: 10,              // 主副标题纵向间隔，单位px，默认为10，
    //字体格式
    textStyle: {
       align: 'center',
       color: '#fff',  // 主标题文字颜色
       fontSize: ds_fontSize(1),
   },
    subtextStyle: { }    //副标题
},`}
    else if(zj ==='图形提示'){c=`tooltip: {//提示框，鼠标悬浮交互时的信息提示
    trigger: "axis",//触发类型，默认（item）数据触发，可选为：item|axis
    formatter: '{a} {b} : {c}',
    //formatter: '{b} {a0}: {c0}{a1}: {c1} {a2}: {c2}%',
    //折线（区域）图、柱状（条形）图、K线图 : {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
    //散点图（气泡）图 : {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
    //地图 : {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
    //饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
    showDelay: 20,             // 显示延迟单位ms
    hideDelay: 100,            // 隐藏单位ms
    transitionDuration : 0.4,  // 动画变换时间单位s
    backgroundColor: 'rgba(0,0,0,0.7)',    // 提示背景颜色，默认为透明度为0.7的黑色
    borderColor: '#333',       // 提示边框颜色
    borderRadius: 4,           // 提示边框圆角，单位px，默认为4
    borderWidth: 0,   
    padding: 5,   
    axisPointer : {            // 坐标轴指示器，坐标轴触发有效
        type : 'line',         // 默认为直线，可选为：'line' | 'shadow'
        lineStyle : {          // 直线指示器样式设置
            color: '#48b',
            width: 2,
            type: 'solid'
        },
        shadowStyle : {         // 阴影指示器样式设置
            width: 'auto',                 // 阴影大小
            color: 'rgba(150,150,150,0.3)'  // 阴影颜色
        }
    },
    textStyle: {
        color: '#fff'
    }
}`}
    else if(zj ==='图例配置'){c=`legend: {
    show: true,
    orient: 'horizontal',      // 布局方式 'horizontal' ¦ 'vertical'
    x: "center",   //水平位置center|left|right|{number}（x坐标，单位px）
    y: "top",   //垂直位置top|bottom|center|{number}（y坐标，单位px）
    //legend的data: 用于设置图例，data内的字符串数组需要与sereis数组内每一个series的name值对应
    data: ['销量', '人员'],
    backgroundColor: 'rgba(0,0,0,0)',
    borderColor: '#ccc',       // 图例边框颜色
    borderWidth: 0,            // 图例边框线宽
    padding: 5,                // 图例内边距
    itemGap: 10,               // 各个item之间的间隔
    itemWidth: 20,             // 图例图形宽度
    itemHeight: 14,            // 图例图形高度
    //字体格式
    textStyle: {
     align: 'center',
     color: '#fff',
     fontSize: 20,
   },
   //图标样式'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
   icon: "diamond",
   //选择模式,默认开启图例选择,false 关闭,设成 'single' 或者 'multiple'使用单选或者多选模式
   selectedMode:true,
   //选中状态
   selected: {
    '销量': true,
    '人员': false
   },
},`}
    else if(zj ==='X轴设定'){c=`xAxis: {    
    //x轴的标签
    data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
    //显示策略，可选为：true（显示）| false（隐藏)
    show: true,
    type: 'category',//坐标轴类型，横轴默认为类目型’category’
    position: 'bottom',    // 位置
    nameLocation: 'end',   // 坐标轴名字位置，支持'start' | 'end'
    boundaryGap: true,     // 类目起始和结束两端空白策略
    //x轴的标签格式
    axisLabel: {
        show: true,
        interval: 'auto',
        rotate: 0,
        margin: 8,
        //样式
        textStyle: {
            color: "#ebf8ac", //X轴文字颜色
         },
    },
    //x轴的轴线格式
    axisLine: {
        show: true, //是否隐藏X轴轴线
        lineStyle: {
            color: '#01FCE3',
            width: 2,
            type: 'solid'
         }
    },
    //x轴的刻度格式
    axisTick: {         // 坐标轴小标记
      show: true,       // 属性show控制显示与否，默认不显示
      interval: 'auto',
      // onGap: null,
      inside : false,    // 控制小标记是否在grid里 
      length :5,         // 属性length控制线长
      lineStyle: {       // 属性lineStyle控制线条样式
        color: '#333',
        width: 1
      }
    },
    splitLine: {           // 分隔线
       show: true,        // 默认显示，属性show控制显示与否
      //onGap: null,
      lineStyle: {      
        color: ['#ccc'],
        width: 1,
        type: 'solid'
      }
   },
    splitArea: {           // 分隔区域
        show: false,       // 默认不显示，属性show控制显示与否
        //onGap: null,
        areaStyle: {       // 属性areaStyle（详见areaStyle）控制区域样式
            color: ['rgba(250,250,250,0.3)','rgba(200,200,200,0.3)']
        }
    }
}
`}
    else if(zj ==='Y轴设定'){c=`yAxis: {
    show: true,
    //坐标轴类型，纵轴默认为数值型’value’
    type: 'value',
    //指定刻度范围
    min: 0,
    max: 50,
    interval:10,
    // 数值型坐标轴默认参数
    position: 'left',      // 位置
    nameLocation: 'end',   // 坐标轴名字位置，支持'start' | 'end'
    nameTextStyle: {},     // 坐标轴文字样式，默认取全局样式
    boundaryGap: [0, 0],   // 数值起始和结束两端空白策略
    splitNumber: 5,        // 分割段数，默认为5
    axisLine: {            // 坐标轴线
        show: true,        // 默认显示，属性show控制显示与否
        lineStyle: {       // 属性lineStyle控制线条样式
            color: '#48b',
            width: 2,
            type: 'solid'
        }
    },
    axisTick: {            // 坐标轴小标记
        show: false,       // 属性show控制显示与否，默认不显示
        inside : false,    // 控制小标记是否在grid里 
        length :5,         // 属性length控制线长
        lineStyle: {       // 属性lineStyle控制线条样式
            color: '#333',
            width: 1
        }
    },
    axisLabel: {      
        show: true,
        rotate: 0,
        margin: 8,
        textStyle: {
            color: function (value, index) {
               return value >= 90 ? 'green' : 'red';
             }
         },
        //数值
        formatter:function (value, index) {
          return value/10000 + '万';
         },
    },
    splitLine: {           // 分隔线
        show: true,        // 默认显示，属性show控制显示与否
        lineStyle: {       // 属性lineStyle（详见lineStyle）控制线条样式
            color: ['#ccc'],
            width: 1,
            type: 'solid'
        }
    },
    splitArea: {           // 分隔区域
        show: false,       // 默认不显示，属性show控制显示与否
        areaStyle: {       // 属性areaStyle（详见areaStyle）控制区域样式
            color: ['rgba(250,250,250,0.3)','rgba(200,200,200,0.3)']
        }
    } 
},
//多坐标的写法
yAxis:[
  //0号坐标
  {
    type: 'value',
     name:'总量',
     position:'left',
   },
   //1号坐标
   {
      type: 'value',
      name:'差异',
      position : 'right',
   },
 ] 
`}
     else if(zj ==='图形系列'){c=`series: [
    {
        name: '销量',
        type: 'bar',
        barWidth: 15,  //宽度
        barGap:'30%', //间距
        data: [5, 20, 36, 10, 10, 20],
        label: {
            show: true, //是否显示数值
            //position: [10, 10], //位置绝对的像素值
            position: ['50%', '50%'], //相对的百分比,'top','bottom','inside'
            rotate:-36, //角度
            formatter: '{b}:{c}' //自定义数据    
        },
        //显示样式
        itemStyle: {
            borderRadius: 10,
            color: "#058cff",
            //渐变色设定
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: "#00FFE3"
                },
                {
                    offset: 1,
                    color: "#4693EC"
                }
            ]),
        },
        //系列外框线格式
        lineStyle: {
            color: "#058cff"
        },
        //系列填充格式面积图
        areaStyle:{
            color: "rgba(5,140,255, 0.2)"
        }, 
        //折线设定,所有标记样式如下
        //'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
        smooth: true, //平滑曲线显示
        showAllSymbol: true, //显示所有图形。
        symbol: "circle", //标记的图形为实心圆
        symbolSize: 10, //标记的大小  
        //标记点
        markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'},
                    {name: '坐标',coord: [10, 20]},
                    {name: '屏幕坐标',x:100,y:200},
                ],
                //标记
                symbol:'pin',
                symbolSize:50,
                symbolRotate:-30,
                //通用格式如上的label
                label:{
                    show:true,
                },
            },
            
        //标记线
        markLine : {
            data : [
                {type : 'average', name: '平均值'},
                {name : '1000', yAxis : 24},
            ]
        },
        
    },
   //高级series设定的方法
     {
        name: legend_label[2],
        data: dataset[legend_label[2]],
        type: 'line',
        yAxisIndex:1, //所在坐标轴,0为默认
        label:{
            show:true,
            formatter:function(param) {
             if (param.value===0) {return '';} else
               {return param.value;}
         }
       }
   },
 
],`}
     else if(zj ==='视觉映射'){c=`visualMap: {
    min: 0,
    max: 100,
    // 两个手柄对应的数值是 4 和 15
    range: [4, 100],
    calculable:true, //是否显示手柄
    itemWidth:20,
    itemHeight:140,
    text:['最大值','最小值'],
    //dimension:1, //指定用数据哪个维度，映射到视觉元素上
    seriesIndex:0, //指用那个系列
    hoverLink:true, //鼠标位置对应的数值图表中对应的图形元素高亮
    // 表示目标系列的视觉样式 和 visualMap-continuous 共有的视觉样式。
    inRange: {
        color: ['#121122', 'rgba(3,4,5,0.4)', 'red'],
        symbolSize: [4, 100]
    },
    // 表示 visualMap-continuous本身的视觉样式，会覆盖共有的视觉样式。
    // 比如，symbolSize 覆盖成为 [30, 100]，而 color 不变。
    controller: {
        inRange: {
            symbolSize: [30, 100]
        }
    }
    
},  `}
     else if(zj ==='工具栏'){c=`toolbox: {
    show: true,
    feature: {
        //辅助线标志
        mark: { show: true },
        //dataZoom，框选区域缩放，自动与存在的dataZoom控件同步，分别是启用，缩放后退
        dataZoom: {
            show: true,
            title: {
                dataZoom: "区域缩放",
                dataZoomReset: "区域缩放后退"
                }
        },
      featureImageIcon : {},     // 自定义图片icon
      featureTitle : {
            mark : '辅助线开关',
            markUndo : '删除辅助线',
            markClear : '清空辅助线',
            dataZoom : '区域缩放',
            dataZoomReset : '区域缩放后退',
            dataView : '数据视图',
            lineChart : '折线图切换',
            barChart : '柱形图切换',
            restore : '还原',
            saveAsImage : '保存为图片'
        }
        dataView: { show: true, readOnly: true },
        //magicType，动态类型切换，支持直角系下的折线图、柱状图、堆积、平铺转换
        magicType: { show: true, type: ["line", "bar"] },
        //restore，还原，复位原始图表
        restore: { show: true },
        //saveAsImage，保存图片（IE8-不支持）,图片类型默认为’png’
        saveAsImage: { show: true }
    }
},
}`}
     else if(zj ==='柱形图'){c=`type:'bar',
barMinHeight: 0,          // 最小高度改为0
// barWidth: null,        // 默认自适应
barGap: '30%',            // 柱间距离，默认为柱形宽度的30%，可设固定值
barCategoryGap : '20%',   // 类目间柱形距离，默认为类目间距的20%，可设固定值
itemStyle: {
    barBorderColor: '#fff',       // 柱条边线
    barBorderRadius: 0,           // 柱条边线圆角，单位px，默认为0
    barBorderWidth: 1,            // 柱条边线线宽，单位px，默认为1
    label: {
        show: false
        position: 可选为 'inside'|'left'|'right'|'top'|'bottom'
    },
    emphasis: {
        focus: 'series' ,  // data
        color: 'xx',
        barBorderColor: 'rgba(0,0,0,0)',   // 柱条边线
        barBorderRadius: 0,                // 柱条边线圆角默认为0
        barBorderWidth: 1,                 // 柱条边线线宽默认为1
        label: {
            show: false
            position: 'inside'|'left'|'right'|'top'|'bottom'
        }
    }
`}
     else if(zj ==='折线图'){c=`type:'line',
itemStyle: {
    color: '',
    label: {
        show: false
        position: 'inside'|'left'|'right'|'top'|'bottom'
        textStyle: null   
    },
    lineStyle: {
        width: 2,
        type: 'solid',
        shadowColor : 'rgba(0,0,0,0)', //默认透明
        shadowBlur: 5,
        shadowOffsetX: 3,
        shadowOffsetY: 3
    },
    emphasis: {
        color: '',
        label: {
            show: false,
        }
    }
},
smooth : false,
symbol: null,         // 拐点图形类型
symbolSize: 2,          // 拐点图形大小
symbolRotate : null,  // 拐点图形旋转控制
showAllSymbol: false    // 标志图形默认只有主轴显示（随主轴标签间隔隐藏策略）
 `}
     else if(zj ==='饼图'){c=`type:'pie',
center : ['50%', '50%'],    // 默认全局居中
radius : [0, '75%'],        //内环外环
clockWise : false,          // 默认逆时针
startAngle: 90,
minAngle: 0,                // 最小角度改为0
selectedOffset: 10,         // 选中是扇区偏移量
itemStyle: {
    color: '',
    borderColor: '#fff',
    borderWidth: 1,
    label: {
        show: true,
        position: 'outer'
        textStyle: null 
    },
    labelLine: {
        show: true,
        length: 20,
        lineStyle: {
            color: '',
            width: 1,
            type: 'solid'
        }
    },
    emphasis: {
       color: '',
        borderColor: 'rgba(0,0,0,0)',
        borderWidth: 1,
        label: {
            show: false
        },
        labelLine: {
            show: false,
            length: 20,
            lineStyle: {
                color: '',
                width: 1,
                type: 'solid'
            }
    }`}
     else if(zj ==='地图'){c=`type:'map',
mapType: 'china',  
mapLocation: {
    x : 'center',
    y : 'center'
    // width    // 自适应
    // height   // 自适应
},
showLegendSymbol : true,       // 显示图例颜色标识（系列标识的小圆点），存在legend时生效
itemStyle: {
    color: '',
    borderColor: '#fff',
    borderWidth: 1,
    areaStyle: {
        color: '#ccc'//rgba(135,206,250,0.8)
    },
    label: {
        show: false,
        textStyle: {
            color: 'rgba(139,69,19,1)'
        }
    },
    emphasis: { // 也是选中样式
        // color: 各异,
        borderColor: 'rgba(0,0,0,0)',
        borderWidth: 1,
        areaStyle: {
            color: 'rgba(255,215,0,0.8)'
        },
        label: {
            show: false,
            textStyle: {
                color: 'rgba(139,69,19,1)'
            }
        }
    }`}
     else if(zj ==='仪表盘'){c=`name:'业务指标',
type:'gauge',
radius:'100%',
splitNumber: 10,       // 分割段数，默认为5
axisLine: {            // 坐标轴线
    lineStyle: {       // 属性lineStyle控制线条样式
        color: [[0.2, '#228b22'],[0.8, '#48b'],[1, '#ff4500']], 
        width: 8
    }
},
axisTick: {            // 坐标轴小标记
    splitNumber: 10,   // 每份split细分多少段
    length :12,        // 属性length控制线长
    lineStyle: {       // 属性lineStyle控制线条样式
        color: 'auto'
    }
},
axisLabel: {           // 坐标轴文本标签，详见axis.axisLabel
    textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
        color: 'auto'
    }
},
splitLine: {           // 分隔线
    show: true,        // 默认显示，属性show控制显示与否
    length :30,         // 属性length控制线长
    lineStyle: {       // 属性lineStyle（详见lineStyle）控制线条样式
        color: 'auto'
    }
},
pointer : {    //指针大小
    width : 5
},
title : {
    show : true,
    offsetCenter: [0, '-40%'],       // x, y，单位px
    textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
        fontWeight: 'bolder'
    }
},
detail : {
    formatter:'{value}%',
    textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
        color: 'auto',
        fontWeight: 'bolder'// 下面data数据的字体设置！！！！
    }
},
data:[{value: 50, name: '完成率'}]`}
    return c;
}