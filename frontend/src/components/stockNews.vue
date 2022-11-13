<template>
  <div ref="tradingview" :id="container" class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    
  </div>

  
</template>

<script>

const SCRIPT_ID = 'tradingview-news-widget-script';
const CONTAINER_ID = 'tradingview-widget-container';
export default {
  props:['scriptID'],
  data() {
    return {
      container: CONTAINER_ID,
      options:
        {
        feedMode: "symbol",
        symbol: this.$store.getters.getStockTicker,
        colorTheme: "dark",
        isTransparent: true,
        displayMode: "regular",
        width: "100%",
        height: "100%",
        locale: "en",
        }
    }
  },
  
  watch:{
    '$store.state.stockTicker' : function()  {
      
      let encodedStock = encodeURIComponent(this.$store.getters.getStockTicker)
      let newURL = `https://s.tradingview.com/embed-widget/timeline/?locale=en&symbol=${encodedStock}#%7B%22frameElementId%22%3A%22tradingview-news-widget-script%22%2C%22symbol%22%3A%22NYSE%3AF%22%2C%22colorTheme%22%3A%22dark%22%2C%22isTransparent%22%3Atrue%2C%22displayMode%22%3A%22regular%22%2C%22width%22%3A%22100%25%22%2C%22height%22%3A%22100%25%22%2C%22utm_source%22%3A%22localhost%22%2C%22utm_medium%22%3A%22widget%22%2C%22utm_campaign%22%3A%22timeline%22%7D`
      
      
      document.getElementById('tradingview-news-widget-script').src = newURL;
      
      
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
      script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-timeline.js';
      script.onload = onload;
      script.textContent = JSON.stringify(this.options)
      
      this.$refs.tradingview.appendChild(script);
    },
    initWidget() {
      // console.log('stock news loaded', this.options)
      // console.log(document.getElementById('tradingview-news-widget-script'))
    },
  },
  mounted() {
    setTimeout(() => {
      this.appendScript(this.initWidget)
    }, 300)

    
  },

  
}
</script>