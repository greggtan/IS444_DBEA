<template>
  <div ref="tradingview" :id="container" class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    
  </div>

  
</template>

<script>

const SCRIPT_ID = 'tradingview-market-movers-widget-script';
const CONTAINER_ID = 'tradingview-widget-container';
export default {
  props:['scriptID'],
  data() {
    return {
      container: CONTAINER_ID,
      options:
        {
       colorTheme: "dark",
        dateRange: "12M",
        exchange: "US",
        showChart: true,
        locale: "en",
        width: "100%",
        height: "100%",
        largeChartUrl: "",
        
        showSymbolLogo: true,
        showFloatingTooltip: true,
        plotLineColorGrowing: "rgba(41, 98, 255, 1)",
        plotLineColorFalling: "rgba(41, 98, 255, 1)",
        gridLineColor: "rgba(240, 243, 250, 0)",
        scaleFontColor: "rgba(120, 123, 134, 1)",
        belowLineFillColorGrowing: "rgba(41, 98, 255, 0.12)",
        belowLineFillColorFalling: "rgba(41, 98, 255, 0.12)",
        belowLineFillColorGrowingBottom: "rgba(41, 98, 255, 0)",
        belowLineFillColorFallingBottom: "rgba(41, 98, 255, 0)",
        symbolActiveColor: "rgba(41, 98, 255, 0.12)"
        }
    }
  },

  methods: {
    canUseDOM() {
      return typeof window !== 'undefined' && window.document && window.document.createElement;
    },
    getScriptElement() {
      return document.getElementById(SCRIPT_ID);
    },
    updateOnloadListener(onload) {
      const script = this.getScriptElement();
      const oldOnload = script.onload;
      return script.onload = () => {
        oldOnload();
        onload();
      };
    },
    scriptExists() {
      return this.getScriptElement() !== null;
    },
    appendScript(onload) {
      if (!this.canUseDOM()) {
        onload();
        return;
      }
      
      if (this.scriptExists()) {
        if (typeof TradingView === 'undefined') {
          this.updateOnloadListener(onload);
          return;
        }
        onload();
        return;
      }
      const script = document.createElement('script');
      script.id = this.scriptID;
      script.type = 'text/javascript';
      script.async = true;
      script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-hotlists.js';
      script.onload = onload;
      script.textContent = JSON.stringify(this.options)
      
      this.$refs.tradingview.appendChild(script);
    },
    initWidget() {
      // console.log('stock screener loaded', this.options)
      
    },
  },
  mounted() {
    setTimeout(() => {
      this.appendScript(this.initWidget)
    }, 300)

    
  },

  
}
</script>