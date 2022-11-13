<template>
  <q-page class="" style="padding-bottom: 150px">

    
  
    <div class="flex justify-between gt-sm">
      <!-- left side -->
      <div class="" style="width: 65vw">
        <!-- TradingView Widget price chart BEGIN -->
        <div class="tradingview-widget-container q-mb-sm" >
              <div id="tradingview_b9c48"></div>
        </div>
        <!-- TradingView Widget END -->



        <!-- <div class="text-white q-mb-sm q-pt-md" style="font-size:30px">
          <span style="font-size:30px; color:#2962ff">{{this.$store.state.pureTicker}}</span> Description
        </div> -->
        <div class="" style="height:350px;">
            <stockDescriptionComponent :scriptID="'tradingview-stock-description'" :key="descriptionKey" />
        </div>


        <!-- <div class="flex items-center" style="color:#7E96B8;font-size:20px; width:100%">
          <div class="" style="width:20vw; margin-left:15px">Time & Date</div>
          <div class="" style="width:40vw; margin-left:17px">News Title</div>
        </div>


        <q-infinite-scroll @load="onLoad" :offset="200" class="newsDiv" style="height:100vh;color:white;overflow:auto">
          <q-item clickable v-ripple v-for="article in news " :key="article.newsID">
            <a :href="article.url"  style="text-decoration:none; color:white">
            <div class="flex items-start no-wrap q-mt-md" style="font-size:20px; width:100%">
              <div class="text-white q-mr-md" style="width:20vw">{{article.timeStamp}}</div>
              <div class="" style="width:40vw">
                <div class="text-white">{{article.headline}}</div>

                <div class="q-mt-sm" style="color:#7E96B8">{{article.source}}</div>
              </div>
            </div>
            </a>
          </q-item>
        
          <template v-slot:loading>
            <div class="row justify-center q-my-md">
              <q-spinner-dots color="primary" size="40px" />
            </div>
          </template>
        </q-infinite-scroll> -->

        <div class="q-mb-xl" style="height:400px">
          <stockNews :scriptID="'tradingview-stock-news'" :key="newsKey"/>
        </div>
        

      </div>

      <!-- right side -->

      
      <div class="" style="width: 25vw; margin-top: 4vh; max-width: 450px">
        <stockMetrics :scriptID="'tradingview-analysis-widget-script'" :refID="'stockMetric'" :key="metricKey"/>
      </div>
    </div>


    <div class="  lt-md">
      <!-- left side -->
      <div class="" style="width: 90vw">
       
        <div class="" style="width:100%; height:60vh">
          <stockPriceGraph ref="myGraph"   />
        </div>
        
        


          <div class="text-white q-mb-sm q-pt-md" style="font-size:30px">
            <span style="font-size:30px; color:#2962ff">{{this.$store.state.pureTicker}}</span> Description
          </div>
          <div class="text-white text-justify" style="width:90vw">
            {{ stockDescription }}
          </div>
          
       

        <div class="text-white q-mb-sm q-pt-md" style="font-size:30px">
            <span style="font-size:30px; color:#2962ff">{{this.$store.state.pureTicker}}</span> Latest News
        </div>

        <div class="flex items-center no-wrap" style="color:#7E96B8;font-size:20px; width:90vw">
          <div class="" style="width:30vw; margin-left:15px">Time & Date</div>
          <div class="" style="width:60vw; margin-left:35px">News Title</div>
        </div>


        <q-infinite-scroll @load="onLoad" :offset="200" class="newsDiv" style="height:50vh;color:white;width:90vw;overflow:auto">
          <q-item clickable v-ripple v-for="article in news " :key="article.newsID">
            <a :href="article.url"  style="text-decoration:none; color:white;">
            <div class="flex items-start no-wrap q-mt-md" style="font-size:20px; width:100%;">
              <div class="text-white q-mr-md" style="width:25vw">{{article.timeStamp}}</div>
              <div class="" style="width:55vw">
                <div class="text-white">{{article.headline}}</div>

                <div class="q-mt-sm" style="color:#7E96B8">{{article.source}}</div>
              </div>
            </div>
            </a>
          </q-item>
        
          <template v-slot:loading>
            <div class="row justify-center q-my-md">
              <q-spinner-dots color="primary" size="40px" />
            </div>
          </template>
        </q-infinite-scroll>

      

      </div>

      <!-- right side -->
      <div class="" style="width: 90vw; margin-top: 4vh;">
        <!-- key metrics div -->
        <div class="q-pa-md" style="background: #131823; border-radius: 8px">
          <div class="text-white" style="font-size: 17px">Key Metrics</div>

          <div
            class="q-pa-md q-mt-lg"
            style="
              border: 0.5px solid grey;
              color: #7e96b8;
              border-radius: 8px;
              font-size: 13px;
            "
          >
            <!-- hype index div, make dynamic -->
            <div class="flex justify-between items-center no-wrap">
              <metricToolTip 
              :metricName="'Hype Index'" 
              :metricDescription="` Measures the relative popularity of the stock based on social media.`" />
              
              <div class="">
                <animated-number :value="hypeIndex" :formatValue="formatToPrice" :duration="duration"/>%
              </div>
            </div>

            <!-- hype ROC div, make dynamic -->
            <div class="flex justify-between items-center no-wrap q-mt-lg">
              <metricToolTip 
              :metricName="'News Sentiment'" 
              :metricDescription="`Measures the relative popularity of the stock based on the news`" />
              
              <div class=""><animated-number :value="newsSentiment" :formatValue="formatToPrice" :duration="duration"/>%</div>
            </div>
          </div>

          <div
            class="q-pa-md q-mt-md"
            style="
              border: 0.5px solid grey;
              color: #7e96b8;
              border-radius: 8px;
              font-size: 13px;
            "
          >
            <!-- Market Cap div, make dynamic -->
            <div class="flex justify-between items-center no-wrap">
              <metricToolTip 
              :metricName="'Market Cap'" 
              :metricDescription="`The total dollar value of a company’s outstanding shares multipled by the share price.`" />
              
              <div class=""><animated-number :value="marketCap" :formatValue="formatToPrice" :duration="duration"/> M</div>
            </div>

            <!-- P/E div, make dynamic -->
            <div class="flex justify-between items-center no-wrap q-mt-lg">
              <metricToolTip 
              :metricName="'P/E'" 
              :metricDescription="`A ratio for valuing a company that measures the current share price divided by the company’s earnings per share.`" />
              
              <div class=""><animated-number :value="peRatio" :formatValue="formatToPrice" :duration="duration"/></div>
            </div>

            <!-- P/B div, make dynamic -->
            <div class="flex justify-between items-center no-wrap q-mt-lg">
              <metricToolTip 
              :metricName="'P/B'" 
              :metricDescription="`A ratio for valuing a company that measures the current share price divided by the company’s book value (calculated using total assets minus intangible assets and liabilities.)`" />
              
              <div class=""><animated-number :value="pbRatio" :formatValue="formatToPrice" :duration="duration"/></div>
            </div>

            <!-- avg volume div, make dynamic -->
            <div class="flex justify-between items-center no-wrap q-mt-lg">
              <metricToolTip 
              :metricName="'Avg Vol'" 
              :metricDescription="` The average daily trading volume over the past 3 months`" />
              
              <div class=""><animated-number :value="avgVolume" :formatValue="formatToPrice" :duration="duration"/> M</div>
            </div>


            <!-- short float div, make dynamic -->
            <div class="flex justify-between items-center no-wrap q-mt-lg">
              <metricToolTip 
              :metricName="'Shares Outstand'" 
              :metricDescription="`The number of shares of the company helf by all its shareholders, including share blocks held by institutional inestors and restricted shares owned by the company’s offiers and insiders`" />
              
              <div class=""><animated-number :value="sharesOutstand" :formatValue="formatToPrice" :duration="duration"/> M</div>
            </div>

            <!-- short float div, make dynamic -->
            <div class="flex justify-between items-center no-wrap q-mt-lg">
              <metricToolTip 
              :metricName="'Employees'" 
              :metricDescription="`The number of employees the company has hired`" />
              
              <div class=""><animated-number :value="employees" :formatValue="formatToPrice" :duration="duration"/></div>
            </div>

            <div class="flex justify-between items-center no-wrap q-mt-lg">
              <metricToolTip 
              :metricName="'Beta'" 
              :metricDescription="`Measures the stock’s volatitility in relation to the overall market (S&P 500)`" />
              
              <div class=""><animated-number :value="beta" :formatValue="formatToPrice" :duration="duration"/></div>
            </div>
          </div>
        </div>

        <div class="text-white q-my-lg" style="font-size: 22px">
          Financial Recap
        </div>

        <!-- income statement div -->
        <div class="" style="border: 1px solid grey; border-radius: 8px">
          <div
            class="q-pl-md q-py-md"
            style="
              border-top-left-radius: 8px;
              border-top-right-radius: 8px;
              background: linear-gradient(138.56deg,#f83b77 1.36%,#627eea 148.23%);
              -khtml-opacity: 0.7d9;
              -moz-opacity: 0.79;
              -ms-filter: ”alpha(opacity=79) ”;
              filter: alpha(opacity=79);
              filter: progid:DXImageTransform.Microsoft.Alpha(opacity=0.79);
              opacity: 0.79;
            "
          >
            <span style="color: white; font-size: 15px">Income Statement</span>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-mt-lg"
            style="color: #7e96b8; font-size: 13px"
          >
          <metricToolTip 
              :metricName="'EBITDA'" 
              :metricDescription="`Earnings Before Interest, Taxes, Depreciation and Amortization. It is a useful metric to evaluate the company’s ability to generate cash flow. `" />
             
            <div :class="[EBITDA>0 ? 'text-green' : 'text-red']"><animated-number :value="EBITDA" :formatValue="formatToPrice" :duration="duration"/> M</div>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-mt-lg"
            style="color: #7e96b8; font-size: 13px"
          >
          <metricToolTip 
              :metricName="'EBIT'" 
              :metricDescription="`Earnings Before Interest and taxes.`" />
            
            <div :class="[EBIT>0 ? 'text-green' : 'text-red']">{{ EBIT }} M</div>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-mt-lg"
            style="color: #7e96b8; font-size: 13px"
          >
          <metricToolTip 
              :metricName="'Net Income'" 
              :metricDescription="`Calculated as revenue minus expenses, interests and taxes.`" />
            
            <div :class="[netIncome>0 ? 'text-green' : 'text-red']">{{ netIncome }} M</div>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-my-lg"
            style="color: #7e96b8; font-size: 13px"
          >
          <metricToolTip 
              :metricName="'Diluted EPS'" 
              :metricDescription="`Calculated using the company's net income divided by the number of outstanding shares of a common stock`" />
          
            <div :class="[dilutedEPS>0 ? 'text-green' : 'text-red']">{{ dilutedEPS }}</div>
          </div>
        </div>

        <!-- balance sheet div -->
        <div class="q-mt-lg" style="border: 1px solid grey; border-radius: 8px">
          <div
            class="q-pl-md q-py-md"
            style="
              border-top-left-radius: 8px;
              border-top-right-radius: 8px;
              background: linear-gradient(221.44deg, #ea40f7 1.36%,#627eea 148.23%);
              -khtml-opacity: 0.7d9;
              -moz-opacity: 0.79;
              -ms-filter: ”alpha(opacity=79) ”;
              filter: alpha(opacity=79);
              filter: progid:DXImageTransform.Microsoft.Alpha(opacity=0.79);
              opacity: 0.79;
            "
          >
            <span style="color: white; font-size: 15px">Balance Sheet</span>
          </div>

          <!-- make dynamic red or green based on value later -->
          <div
            class="flex justify-between items-center no-wrap q-px-md q-mt-lg"
            style="color: #7e96b8; font-size: 13px"
          >
          <metricToolTip 
              :metricName="'ROI'" 
              :metricDescription="'Measures the efficiency of the company’s investments. It is calculated by dividing the company’s net gain of the investment over the cost of the investment'" />
            
            <div  :class="[ROI>0 ? 'text-green' : 'text-red']">{{ ROI }}%</div>
          </div>

          <!-- make dynamic red or green based on value later -->
          <div
            class="flex justify-between items-center no-wrap q-px-md q-mt-lg"
            style="color: #7e96b8; font-size: 13px"
          >
          <metricToolTip 
              :metricName="'ROE'" 
              :metricDescription="'Measures the profitabilit of a compnay relative to the capital that shareholders have invested. It is calcuklated by dividing the company’s annual net income over shareholder’s equity '" />
            
            <div :class="[ROE>0 ? 'text-green' : 'text-red']">{{ ROE }}%</div>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-my-lg"
            style="color: #7e96b8; font-size: 13px"
          >
          <metricToolTip 
              :metricName="'Quick Ratio'" 
              :metricDescription="'Used to measure the company’s ability to pay for short-term obligations. It is calculated by dividing the current assets over the current liabilities '" />
            
            <div class="">{{ quickRatio }}</div>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-my-lg"
            style="color: #7e96b8; font-size: 13px"
          >
          <metricToolTip 
              :metricName="'Current Ratio'" 
              :metricDescription="'Used to measure the company’s ability to pay for short-term obligations with its liquid assets. It is calculated by dividing the (current assets - invesntories) over the current liabilities'" />
            
            <div class="">{{ currentRatio }}</div>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-my-lg"
            style="color: #7e96b8; font-size: 13px"
          >
           <metricToolTip 
              :metricName="'Debt / Equity'" 
              :metricDescription="' Measures the extent of the company’s financial leverage. It is calculated by dividing the liabilities by stockholder’s equity. '" />
          
            <div class="">{{ debtEquity }}</div>
          </div>
        </div>

        <!-- cash flows div -->
        <div class="q-mt-lg" style="border: 1px solid grey; border-radius: 8px">
          <div
            class="q-pl-md q-py-md"
            style="
              border-top-left-radius: 8px;
              border-top-right-radius: 8px;
              background: linear-gradient(138.56deg, #8060ff 1.36%, #076beb 148.23%);
              -khtml-opacity: 0.7d9;
              -moz-opacity: 0.79;
              -ms-filter: ”alpha(opacity=79) ”;
              filter: alpha(opacity=79);
              filter: progid:DXImageTransform.Microsoft.Alpha(opacity=0.79);
              opacity: 0.79;
            "
          >
            <span style="color: white; font-size: 15px">Cash Flows</span>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-mt-lg"
            style="color: #7e96b8; font-size: 13px"
          >
          <metricToolTip 
              :metricName="'Dividend / Share'" 
              :metricDescription="' Calculated using the amount company pays out in dividends annually divided by the number of outstanding shares of a common stock '" />
          
            <div class="">{{ dividendShare }}M</div>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-mt-lg"
            style="color: #7e96b8; font-size: 13px"
          >
             <metricToolTip 
              :metricName="'Dividend %'" 
              :metricDescription="'Measures the percentage of how much a company pays out in dividends annually relative to its stock price. '" />
            
            <div class="">{{ dividendPercent }}%</div>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-mt-lg"
            style="color: #7e96b8; font-size: 13px"
          >
            <metricToolTip 
              :metricName="'Operating Cash Flow'" 
              :metricDescription="'Measures the amount of cash generated by a company’s normal business operations'" />
            
            <div class="">{{ operatingCashFlow }}M</div>
          </div>

          <div
            class="flex justify-between items-center no-wrap q-px-md q-my-lg"
            style="color: #7e96b8; font-size: 13px"
          >
            <metricToolTip 
              :metricName="'Free Cash Flow'" 
              :metricDescription="'Amount of money the company remains after paaying all of its financial obliations'" />
            
            <div class="">{{freeCashFlow }}M</div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import TradingVue from "trading-vue-js";
import metricToolTip from "../components/metricToolTip.vue"

import stockDescriptionComponent from 'src/components/stockDescription.vue';
import stockNews from 'src/components/stockNews.vue';
import stockPriceGraph from 'src/components/stockPriceGraph.vue';
import stockMetrics from 'src/components/stockMetrics.vue';

import AnimatedNumber from "animated-number-vue";
var iso8601 = require('iso8601-convert')

export default {
  components: { TradingVue, metricToolTip, stockDescriptionComponent,stockNews, AnimatedNumber,stockPriceGraph, stockMetrics },

  data() {
    return {
      // tab: "5min",
      current: 1,
      duration:900,
      metricKey:'stock',
      descriptionKey:'abc',
      newsKey:'def',

      hypeIndex: "",
      hypeROC: "",
      sentimentROC: "",
      stockDescription:'',
      newsSentiment:'',

      marketCap: "",
      peRatio: "",
      pbRatio: "",
      avgVolume: "",
      employees: "",
      sharesOutstand: "",
      beta: "",

      EBITDA: "",
      EBIT: "",
      netIncome: "",
      dilutedEPS: "",

      ROI: "",
      ROE: "",
      quickRatio: "",
      currentRatio: "",
      debtEquity: "",

      dividendShare: "",
      dividendPercent: "",
      operatingCashFlow: "",
      freeCashFlow: "",

      news:[],
      allNews:[],
      currentPage:1,
      eachPageNoItems:3,

      
      stockData:{},
    };
  },
  async mounted() {
    // let urls=[
    //   `http://202.55.80.86:80/api/v1/FrontIncome?tickerAbbreviation=${this.$store.state.pureTicker}`,   //income statement
    //   `http://202.55.80.86:80/api/v1/FrontBalance?tickerAbbreviation=${this.$store.state.pureTicker}`,  //balance sheet
    //   `http://202.55.80.86:80/api/v1/FrontCash?tickerAbbreviation=${this.$store.state.pureTicker}`,     //cash flows
    //   `http://202.55.80.86:80/api/v1/FrontBasic?tickerAbbreviation=${this.$store.state.pureTicker}`,     //key metrics bottom div
    //   `http://202.55.80.86:80/api/v1/CompanyDesc?tickerAbbreviation=${this.$store.state.pureTicker}`,   //description,
    //   `http://202.55.80.86:65500/api/v1/News?tickerAbbreviation=${this.$store.state.pureTicker}&periodStart=2021%2F09%2F21&periodEnd=2021%2F09%2F28`,
    //   `http://202.55.80.86:65500/api/v1/NewsSentiment?tickerAbbreviation=${this.$store.state.pureTicker}`   
    //   ]


    // const financialRecap = await Promise.all(urls.map(async url => {
    // const resp = await fetch(url);
    // return resp.json();
    // }));

    // // console.log('financial recap array: ',financialRecap)
    // //income statement
    // this.EBITDA = Math.round(parseFloat(financialRecap[0][0].value) * 100) / 100
    // this.EBIT =  Math.round(parseFloat(financialRecap[0][1].value) * 100) / 100
    // this.netIncome =  Math.round(parseFloat(financialRecap[0][2].value) * 100) / 100
    // this.dilutedEPS =  Math.round(parseFloat(financialRecap[0][3].value) * 100) / 100 

    // //balance sheet
    // this.ROI = Math.round(parseFloat(financialRecap[1][0].value) * 100) / 100
    // this.ROE =  Math.round(parseFloat(financialRecap[1][1].value) * 100) / 100
    // this.quickRatio =  Math.round(parseFloat(financialRecap[1][2].value) * 100) / 100
    // this.currentRatio =  Math.round(parseFloat(financialRecap[1][3].value) * 100) / 100 
    // this.debtEquity =  Math.round(parseFloat(financialRecap[1][4].value) * 100) / 100 

    // //cash flows
    // this.dividendShare = Math.round(parseFloat(financialRecap[2][0].value) * 100) / 100
    // this.dividendPercent =  Math.round(parseFloat(financialRecap[2][1].value) * 100) / 100
    // this.operatingCashFlow =  Math.round(parseFloat(financialRecap[2][2].value) * 100) / 100
    // this.freeCashFlow =  Math.round(parseFloat(financialRecap[2][3].value) * 100) / 100 

    // //key metrics bottom div
    // this.marketCap = Math.round(parseFloat(financialRecap[3][0].value) * 100) / 100
    // this.peRatio =  Math.round(parseFloat(financialRecap[3][1].value) * 100) / 100
    // this.pbRatio =  Math.round(parseFloat(financialRecap[3][2].value) * 100) / 100
    // this.avgVolume =  Math.round(parseFloat(financialRecap[3][3].value) * 100) / 100 
    // this.employees =  (Math.round(parseFloat(financialRecap[3][4].value) * 100) / 100)
    // this.sharesOutstand =  Math.round(parseFloat(financialRecap[3][5].value) * 100) / 100 
    // this.beta =  Math.round(parseFloat(financialRecap[3][6].value) * 100) / 100 


    // this.stockDescription = financialRecap[4].value

    
    // this.allNews = financialRecap[5]

    // // hype data
    // this.hypeIndex = financialRecap[6][0].buzz
    // this.newsSentiment = financialRecap[6][0].companyNewsScore
    
    
    
    // for (let i=0; i<this.allNews.length; i++){
    //   let timeDateArray = this.allNews[i].timeStamp.split('T')
    //   let newTimeDate = `${timeDateArray[0]} at ${timeDateArray[1]}`
    //   // final step
    //   this.allNews[i].timeStamp = newTimeDate
    //   // console.log(this.news[i].timeStamp)
    // }

    // this.news = this.allNews.slice(0,3)
    // // console.log(this.news)

    // overall price graph
    new TradingView.MediumWidget({
      symbols: [[`${this.$store.getters.getStockTicker}`]],
      chartOnly: false,
      width: "100%",
      height: "520px",
      locale: "en",
      colorTheme: "dark",
      gridLineColor: "rgba(42 ,46, 57, 0)",
      trendLineColor: "#2962FF",
      fontColor: "#787B86",
      underLineColor: "rgba(41, 98, 255, 0.3)",
      underLineBottomColor: "rgba(41, 98, 255, 0)",
      isTransparent: true,
      autosize: true,
      container_id: "tradingview_b9c48",
      showFloatingTooltip:true

    });


   
    // this.$refs.myGraph.$forceUpdate()
  


  },


  
  watch:{
    '$store.state.stockTicker' : async function()  {
      this.$refs.myGraph.$forceUpdate()
      this.metricKey+="a"
      this.descriptionKey +='a'
      this.newsKey +='a'
    //   let urls=[
    //   `http://202.55.80.86:80/api/v1/FrontIncome?tickerAbbreviation=${this.$store.state.pureTicker}`,   //income statement
    //   `http://202.55.80.86:80/api/v1/FrontBalance?tickerAbbreviation=${this.$store.state.pureTicker}`,  //balance sheet
    //   `http://202.55.80.86:80/api/v1/FrontCash?tickerAbbreviation=${this.$store.state.pureTicker}`,     //cash flows
    //   `http://202.55.80.86:80/api/v1/FrontBasic?tickerAbbreviation=${this.$store.state.pureTicker}`,     //key metrics bottom div
    //   `http://202.55.80.86:80/api/v1/CompanyDesc?tickerAbbreviation=${this.$store.state.pureTicker}`,   //description
    //    `http://202.55.80.86:65500/api/v1/News?tickerAbbreviation=${this.$store.state.pureTicker}&periodStart=2021%2F09%2F21&periodEnd=2021%2F09%2F28`,
    //    `http://202.55.80.86:65500/api/v1/NewsSentiment?tickerAbbreviation=${this.$store.state.pureTicker}`,     //key metrics bottom div
    //   ]


    // const financialRecap = await Promise.all(urls.map(async url => {
    // const resp = await fetch(url);
    // return resp.json();
    // }));

    // // console.log('financial recap array: ',financialRecap)
    // //income statement

    


    // this.EBITDA = Math.round(parseFloat(financialRecap[0][0].value) * 100) / 100
    // this.EBIT =  Math.round(parseFloat(financialRecap[0][1].value) * 100) / 100
    // this.netIncome =  Math.round(parseFloat(financialRecap[0][2].value) * 100) / 100
    // this.dilutedEPS =  Math.round(parseFloat(financialRecap[0][3].value) * 100) / 100 

    // //balance sheet
    // this.ROI = Math.round(parseFloat(financialRecap[1][0].value) * 100) / 100
    // this.ROE =  Math.round(parseFloat(financialRecap[1][1].value) * 100) / 100
    // this.quickRatio =  Math.round(parseFloat(financialRecap[1][2].value) * 100) / 100
    // this.currentRatio =  Math.round(parseFloat(financialRecap[1][3].value) * 100) / 100 
    // this.debtEquity =  Math.round(parseFloat(financialRecap[1][4].value) * 100) / 100 

    // //cash flows
    // this.dividendShare = Math.round(parseFloat(financialRecap[2][0].value) * 100) / 100
    // this.dividendPercent =  Math.round(parseFloat(financialRecap[2][1].value) * 100) / 100
    // this.operatingCashFlow =  Math.round(parseFloat(financialRecap[2][2].value) * 100) / 100
    // this.freeCashFlow =  Math.round(parseFloat(financialRecap[2][3].value) * 100) / 100 

    // //key metrics bottom div
    // this.marketCap = Math.round(parseFloat(financialRecap[3][0].value) * 100) / 100
    // this.peRatio =  Math.round(parseFloat(financialRecap[3][1].value) * 100) / 100
    // this.pbRatio =  Math.round(parseFloat(financialRecap[3][2].value) * 100) / 100
    // this.avgVolume =  Math.round(parseFloat(financialRecap[3][3].value) * 100) / 100 
    // this.employees =  Math.round(parseFloat(financialRecap[3][4].value) * 100) / 100 
    // this.sharesOutstand =  Math.round(parseFloat(financialRecap[3][5].value) * 100) / 100 
    // this.beta =  Math.round(parseFloat(financialRecap[3][6].value) * 100) / 100 


    // this.stockDescription = financialRecap[4].value

    // this.allNews = financialRecap[5]

    // // hype data
    // this.hypeIndex = financialRecap[6][0].buzz
    // this.newsSentiment = financialRecap[6][0].companyNewsScore


  
    // for (let i=0; i<this.allNews.length; i++){
    //   let timeDateArray = this.allNews[i].timeStamp.split('T')
    //   let newTimeDate = `${timeDateArray[0]} at ${timeDateArray[1]}`
    //   // final step
    //   this.allNews[i].timeStamp = newTimeDate
    
    // }
    // this.news = this.allNews.slice(0,3)
    // // console.log(this.news)

      // UPDATE the tradingview widget
      new TradingView.MediumWidget({
      symbols: [[`${this.$store.getters.getStockTicker}`]],
      chartOnly: false,
      width: "65vw",
      height: "520px",
      locale: "en",
      colorTheme: "dark",
      gridLineColor: "rgba(42 ,46, 57, 0)",
      trendLineColor: "#2962FF",
      fontColor: "#787B86",
      underLineColor: "rgba(41, 98, 255, 0.3)",
      underLineBottomColor: "rgba(41, 98, 255, 0)",
      isTransparent: true,
      autosize: true,
      container_id: "tradingview_b9c48",
    });


    },
  },
  methods: {
    formatToPrice(outstandingLoans) {
      return `<span>${Number(outstandingLoans).toFixed(2)}</span>`;
    },
     onLoad (index, done) {
      setTimeout(() => {
        if (this.news){
          this.currentPage +=1
          if (this.currentPage*this.eachPageNoItems > this.allNews.length){
            done()
            return
          }
          this.news = this.news.concat(this.allNews.slice((this.currentPage*this.eachPageNoItems)-this.eachPageNoItems,this.currentPage*this.eachPageNoItems))
          
          

          done()
        }
          
        
      }, 2000)
    }
    
  },
};
</script>

<style lang="scss">
.newsDiv::-webkit-scrollbar {
  width: 5px;
}

.newsDiv::-webkit-scrollbar-track {
  border-radius: 5px;
}

.newsDiv::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: #49576b;
}
</style>

