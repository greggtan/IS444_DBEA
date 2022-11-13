<template>
  <q-page class="" style="padding-bottom: 100px; overflow-x: hidden">
    
    <div class="q-mx-xl gt-sm" style="overflow:hidden">
      <div
        class="q-mx-sm flex column justify-between no-wrap"
        style="overflow:hidden;height:88vh"
      >
        <div class="flex items-center justify-around no-wrap">
          <div class="" style="">
            <div class="flex items-center no-wrap" style="font-size: 4.5vw">
              <div class="text-white q-mr-sm">Sentient</div>
              <div
                class="q-px-md"
                style="border-radius: 5px; background: #00ccc3"
              >
                charts
              </div>
            </div>

            <div
              class="q-mt-md"
              style="height: 4px; width: 18vw; background: #00ccc3"
            ></div>

            <div class="text-white q-mt-xl" style="font-size: 2vw">
              <span style="font-weight: 500; color: #00ccc3"
                >Fundamental, technical,
                <span style="font-weight: 400; color: white">and</span> social
                media</span
              >
              analysis <br />made easy.
            </div>
          </div>

         

          <div class="" style="width: 33vw">
            <Lottie
              :options="defaultOptions"
              v-on:animCreated="handleAnimation"
            />
          </div>
        </div>

        <div class="" style="position:absolute;top:80vh;left:50%;cursor:pointer">
          <div class="bouncing-mouse " >
            <div class="scroller"></div>
          </div>
        </div>

      </div>

      <div class="flex justify-between items-center q-my-xl">
        <div
          class=""
          data-aos="fade-right"
          data-aos-duration="500"
          data-aos-offset="200"
          data-aos-easing="ease-in-sine"
          style="height: 81vh; width: 44vw"
        >
          <div
            class="q-mb-md"
            style="font-weight: 500; font-size: 30px; color: #ffffff"
          >
            Stock Market Hotlist
          </div>
          <stockMarketMovers :scriptID="'tradingview-market-movers'" />
        </div>

        <div
          class=""
          data-aos="fade-left"
          data-aos-offset="200"
          data-aos-duration="500"
          data-aos-easing="ease-in-sine"
          style="height: 81vh; width: 44vw"
        >
          <div
            class="q-mb-md"
            style="font-weight: 500; font-size: 30px; color: #ffffff"
          >
            Stock Market Latest News
          </div>
          <stockNewsHome :scriptID="'tradingview-news-home'" />
        </div>
      </div>

      <div
        class=""
        data-aos="fade-up"
        data-aos-easing="ease-in-sine"
        data-aos-offset="300"
        data-aos-duration="500"
        style="margin-top: 20vh"
      >
        <div class="" style="font-weight: 500; font-size: 30px; color: #ffffff">
          Stock Overview
        </div>

        <div class="q-mt-sm" style="height: 81vh">
          <stockScreener :scriptID="'tradingview-stock-screener'" />
        </div>
      </div>
    </div>

    <!-- responsive -->
    <div class="q-mx-xl lt-md">
      <div
        class="q-mx-sm flex column  items-center no-wrap  "
        style=""
      >
       
          <!-- top stuff div -->
          <div class="q-mt-xl" style="">
            <div class="flex items-center justify-center no-wrap" style="font-size: 7vw">
              <div class="text-white q-mr-sm" style="border-bottom:4px solid #00ccc3">Sentient</div>
              <div
                class="q-px-md"
                style="border-radius: 5px; background: #00ccc3"
              >
                charts
              </div>
            </div>

            <div class="text-white q-mt-xl text-center" style="font-size: 3vw">
              <span style="font-weight: 500; color: #00ccc3"
                >Fundamental, technical,
                <span style="font-weight: 400; color: white">and</span> social
                media</span
              >
              analysis <br />made easy.
            </div>
          </div>

          

          <div class="" style="width: 40vw">
            <Lottie
              :options="defaultOptions"
              v-on:animCreated="handleAnimation"
            />
          </div>
        

        <div
          class="arrow bounce text-white flex column q-mb-md"
          style="cursor: pointer; margin-top:15vh"
          @click="handleScroll()"
        >
          <div class="q-mb-sm" style="font-size: 2vw">Scroll to begin</div>
          <a class="fa fa-arrow-down fa-2x"></a>
        </div>
      </div>

      <div class="flex justify-between items-center column  " style="margin-top:5vh">
        <div
          class="q-mb-xl"
          data-aos="fade-right"
          data-aos-duration="500"
          data-aos-offset="200"
          data-aos-easing="ease-in-sine"
          style="height: 81vh; width: 80vw"
        >
          <div
            class="q-mb-md"
            style="font-weight: 500; font-size: 30px; color: #ffffff"
          >
            Stock Market Hotlist
          </div>
          <stockMarketMovers :scriptID="'tradingview-market-movers-resp'" />
        </div>

        <div
          class=""
          data-aos="fade-left"
          data-aos-offset="200"
          data-aos-duration="500"
          data-aos-easing="ease-in-sine"
          style="height: 81vh; width: 80vw; margin-top:90px"
        >
          <div
            class="q-mb-md"
            style="font-weight: 500; font-size: 30px; color: #ffffff"
          >
            Stock Market Latest News
          </div>
          <stockNewsHome :scriptID="'tradingview-news-home-widget-script-resp'"
          />
        </div>
      </div>

      <div
        class=""
        data-aos="fade-up"
        data-aos-easing="ease-in-sine"
        data-aos-offset="300"
        data-aos-duration="500"
        style="margin-top: 20vh"
      >
        <div class="" style="font-weight: 500; font-size: 30px; color: #ffffff">
          Stock Overview
        </div>

        <div class="q-mt-sm" style="height: 81vh">
          <stockScreener :scriptID="'tradingview-stockScreener-resp'" />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { scroll } from "quasar";
import { createChart } from "lightweight-charts";
import Lottie from "vue-lottie";
import * as animationData from "./home.json";

import stockScreener from "src/components/stockScreener.vue";
import stockNewsHome from "src/components/stockNewsHome.vue";
import stockMarketMovers from "src/components/stockMarketMovers.vue";
const { getScrollTarget, setScrollPosition } = scroll;

export default {
  components: {
    Lottie,
    stockScreener,
    stockNewsHome,
    stockMarketMovers,
  },
  data() {
    return {
      defaultOptions: {
        animationData: animationData.default,
        loop: 1,
        autoplay: true,
      },
      animationSpeed: 1,
      alert: false,
      width: window.innerWidth / 6,
      height: window.innerHeight / 5,
      windowWidth: window.innerWidth,

     
    };
  },
  mounted() {
    // console.log(this.$store.state.accessToken);
    AOS.init({});
  },
  methods: {
    handleScroll() {
      const ele = document.getElementById("homeChartsDiv"); // You need to get your element here
      const target = getScrollTarget(ele);
      const offset = ele.scrollHeight;
      const duration = 500;
      setScrollPosition(target, offset, duration);
    },

    handleAnimation: function (anim) {
      this.anim = anim;
    },
  },
};
</script>

<style scoped>
a {
  color: white;
  text-decoration: none;
}

.bouncing-mouse{
  width: 0.2vw;
    bottom: 0;
    padding: 10px 15px;
    height: 35px;
    border: 2px solid #fff;
    border-radius: 25px;
    opacity: .75;
    box-sizing: content-box;
    -webkit-animation: bounce 2s infinite;
    animation: bounce 2s infinite;
}

.scroller{
  width: 3px;
    height: 10px;
    border-radius: 25%;
    background-color: #fff;
    -webkit-animation-name: scroller;
    animation-name: scroller;
    -webkit-animation-duration: 2.2s;
    animation-duration: 2.2s;
    -webkit-animation-timing-function: cubic-bezier(.15,.41,.69,.94);
    animation-timing-function: cubic-bezier(.15,.41,.69,.94);
    -webkit-animation-iteration-count: infinite;
    animation-iteration-count: infinite;
}

@keyframes bounce{
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
}
40% {
    transform: translateY(-30px);
}
60% {
    transform: translateY(-15px);
}
}

@keyframes scroller{
  0% {
    opacity: 0;
}
10% {
    transform: translateY(0);
    opacity: 1;
}

100% {
    transform: translateY(15px);
    opacity: 0;
}
}
</style>
