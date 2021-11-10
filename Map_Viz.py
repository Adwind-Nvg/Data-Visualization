#Genral Routines
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
import webbrowser

geo = Geo()
geo.add_schema(maptype="china")
geo.add("", [("马鞍山", 90), ("南京", 80), ("扬州", 70), ("上海", 30), ("芜湖", 50), ("绩溪", 40), ("云林", 40), ("台北", 30), ("合肥", 15), ("南昌", 5), ("杭州", 5), ("北京", 5),("嘉义", 5), ("香港",5), ("海口", 5), ("呼和浩特",5),("重庆", 5)], type_=ChartType.EFFECT_SCATTER)
geo.add("Four Years Routes",[('马鞍山', '南京'), ('马鞍山', '芜湖'), ('南京', '扬州'), ('绩溪', '台北'), ('云林', '台北'), ('云林', '嘉义'), ('南京', '南昌'), ('绩溪', '北京'),('杭州', '香港'),('南京', '合肥'), ('绩溪','呼和浩特'),('南京','海口'),('香港','重庆'),('绩溪', '上海')],
      type_=ChartType.LINES,
      effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=6,  color="blue"), linestyle_opts=opts.LineStyleOpts(curve=0.2), is_large=True)
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=True),)
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="My Four Years College Life"))
geo.render_notebook()
geo.render("FY.html")
webbrowser.open("FY.html")

#Most of my COVID work is inside my Province
#I converted my time of days in 0-5 scale for the convenience of doing heatmap
from pyecharts import Geo
keys = ['黄山市', '马鞍山市', '芜湖市', '宣城市', '池州市', '宿州市', '合肥市', '滁州市', '铜陵市', '安庆市']
values = [1.0, 4.66, 2.67, 1.88, 1.05, 4.05, 1.38, 5.77, 3.73, 3.35]
geo = Geo("Work places and Time Heatmap of Anhui Province", "Made by Abram_Chan", title_color = "#D26900", title_pos="left", width=800, height=600, background_color='#ADFEDC')
geo.add("",keys, values, maptype='安徽', visual_range=[0, 6], type = 'effectScatter', visual_text_color="#D26900", symbol_size=35, is_visualmap= True, is_roam = True)
geo.render(path="COVID.html")
webbrowser.open("COVID.html")

#To be more specific, as you can tell from the heat map above, one city I stayed for the most of my time
from pyecharts import Map 
attr = ['和县','当涂县','花山区','雨山区']
values = [19, 70, 100, 100 ]
map3 = Map("马鞍山市", width=600, height=400)
map3.add("", attr, values, maptype='马鞍山', is_visualmap=True, visual_text_color='#000')
map3.render(path="马鞍山.html")
webbrowser.open("马鞍山.html")

#Also it wouldnt hurt to add places that I have been to when I studied in Taiwan
value = [1, 1, 1, 10, 15, 15, 20, 25, 30, 35, 40, 40, 45, 50, 55]   #赋值显示色差
attr = ['新北市', '台北市', '基隆市', '桃园市', '新竹县', '新竹市', '苗栗县',
      '台中市', '彰化县', '云林县', '嘉义县', '嘉义市', '台南市', '高雄市', '屏东县']
map = Map("ROC", width=1200, height=600)
map.add("", attr, value, maptype='台湾', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render(path = "ROC.html")
webbrowser.open("ROC.html")


