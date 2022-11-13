<template>
  <div :ref="refID"  class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    
  </div>

  
</template>

<script>

// const SCRIPT_ID = 'tradingview-analysis-widget-script';
const CONTAINER_ID = 'tradingview-widget-container';
export default {
    props:['scriptID','refID'],
  data() {
    return {
      container: CONTAINER_ID,
      options:
        {
        interval: "1m",
        width: "100%",
        isTransparent: true,
        height: "100%",
        symbol: this.$store.getters.getStockTicker,
        showIntervalTabs: true,
        locale: "en",
        colorTheme: "dark"
        }
    }
  },

  methods: {
    canUseDOM() {
      return typeof window !== 'undefined' && window.document && window.document.createElement;
    },
    getScriptElement() {
      return document.getElementById(this.scriptID);
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
      script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js';
      script.onload = onload;
      script.textContent = JSON.stringify(this.options)
      
      

      this.$refs[this.refID].appendChild(script);
    },
    initWidget() {
      // console.log('stock analysis screener loaded', this.options)
      
    },
  },
  mounted() {
    setTimeout(() => {
      this.appendScript(this.initWidget)
    }, 300)

    
  },
  
  
}
</script>