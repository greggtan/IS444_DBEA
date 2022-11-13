<template>
  <q-page style="padding-bottom: 200px">




    <div class="flex justify-around no-wrap gt-sm">
      <div class="" style="width: 60vw">
        <div class="flex items-center justify-between">
          <!-- trading view widget -->
          <div class="tradingview-widget-container q-mb-sm">
            <div id="tradingview_b9c48" style="width: 20vw"></div>
          </div>
        </div>

        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
          <div id="tradingview_2e23d" style="width: 60vw; height: 115vh"></div>
        </div>
        <!-- TradingView Widget END -->
      </div>

      <div
        class="q-px-md q-pb-md flex column justify-between  "
        style="background: #131823; border-radius: 8px; width: 25vw;"
      >
      
          <div class="" style="height:400px;">
            <stockAnalysis :scriptID="'tradingview-analysis-widget-script'" :refID="'gauge'"></stockAnalysis>
          </div>
          
          <!-- hype index gauge -->
          <div class="" >
            <gaugeChart
              v-if="stockGauge"
              :gaugeHeader="'Weekly Hype Index'"
              :gaugeValue="fordGauge.hypeIndex"
              :metricDescription="'Measures the relative popularity of the stock on social media platforms.'"
            />
          </div>

          <!-- Hype ROC gauge -->
          <div class="q-mt-lg " >
            <gaugeChart
              v-if="stockGauge"
              :gaugeHeader="'Weekly Company News Score'"
              :gaugeValue="fordGauge.hypeIndex"
              :metricDescription="'Measures the relative popularity of the stock on news platforms.'"
            />
          </div>


         
          
       
      </div>
    </div>
  </q-page>
</template>



<script>
import { TradingVue, DataCube } from "trading-vue-js";
import fordData1min from "./fordData1min.json";
import fordData5min from "./fordData5min.json";
// import TestOverlay from "./TestOverlay.vue";

import stockAnalysis from "src/components/stockAnalysis.vue";
import stockPriceGraph from "src/components/stockPriceGraph.vue";
export default {
  name: "app",
  components: {
    stockAnalysis,
    gaugeChart: require("../components/gauge.vue").default,
    stockPriceGraph: require("../components/stockPriceGraph.vue").default,
  },

  data() {
    return {
      chart: null,
      // overlays: [TestOverlay],
      width: window.innerWidth / 1.7,
      height: window.innerHeight,
      colors: {
        colorBack: "transparent",
        colorGrid: "#eee",
        colorText: "#333",
      },
      hypeIndex: "",
      newsScore: "",
      // remove this fordgauge and google gauge and change to api backend call
      fordGauge: {
        hypeIndex: 78,
        hypeROC: 50,
        overallSentimentIndex: 100,
        newsSentimentIndex: 37,
      },
      googleGauge: {
        hypeIndex: 19,
        hypeROC: 92,
        overallSentimentIndex: 74,
        newsSentimentIndex: 28,
      },
      fordGauge5: {
        hypeIndex: 75,
        hypeROC: 12,
        overallSentimentIndex: 38,
        newsSentimentIndex: 56,
      },
      googleGauge5: {
        hypeIndex: 27,
        hypeROC: 88,
        overallSentimentIndex: 52,
        newsSentimentIndex: 48,
      },

      stockGauge: null,
    };
  },
  methods: {},
  async mounted() {
    

    if (this.$store.state.stockTicker == "NYSE:F") {
      this.stockGauge = this.fordGauge;
    } else {
      this.stockGauge = this.googleGauge;
    }
    new TradingView.MediumWidget({
      symbols: [[`${this.$store.getters.getStockTicker}`]],
      chartOnly: false,
      width: "65vw",
      height: "130px",
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

    new TradingView.widget({
      autosize: true,
      
      symbol: `${this.$store.getters.getStockTicker}`,
      interval: "D",
      timezone: "Etc/UTC",
      theme: "dark",
      style: "1",
      locale: "en",
      toolbar_bg: "#f1f3f6",
      enable_publishing: false,
      hide_side_toolbar: false,
      save_image: false,
      container_id: "tradingview_2e23d",
    });
  },
  // for any searches while on the page
  watch: {
    "$store.state.stockTicker": async function () {
      

      if (this.$store.state.stockTicker == "NYSE:F") {
        this.stockGauge = this.fordGauge;
      } else {
        this.stockGauge = this.googleGauge;
      }
      new TradingView.MediumWidget({
        symbols: [[`${this.$store.getters.getStockTicker}`]],
        chartOnly: false,
        width: "65vw",
        height: "130px",
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
};
</script>

<style lang="scss" scoped>
.inner-text {
  // allow the text to take all the available space in the svg on top of the gauge
  height: 100%;
  width: 100%;

  span {
    max-width: 100px;
    color: red;
  }
}
</style> 
