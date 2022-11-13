<template>
  <q-layout view="lHh Lpr lFf">
    <!-- Header div add gt-sm to class later for responsive-->
    <div
    v-show="!this.$route.fullPath.includes('/login') && !this.$route.fullPath.includes('/admin')"
      class="text-white flex justify-between items-center no-wrap gt-sm"
    >
      <div class="flex items-center no-wrap">
        <!-- <div
          class="q-mx-xl"
          style="font-size: 35px; cursor: pointer"
          @click="$router.push('/home')"
        >
          <img
            src="statics/logo-white.png"
            alt=""
            style="width: 15vw; margin-top: 10px"
          />
        </div> -->

        <q-select
          v-show="
          !this.$route.fullPath.includes('/login') &&
          !this.$route.fullPath.includes('/giro') 
        "
          dense
          behavior="menu"
          v-model="model"
          use-input
          hide-selected
          fill-input
          input-debounce="0"
          dropdown-icon="expand_more"
          input-style="color: white;"
          style="
            background-color: #1a3f6a;
            border-radius: 100px;
            width: 30vw;
            color: white;
          "
          class="myDropdown q-ml-lg"
          rounded
          outlined
          :options="options"
          @filter="filterFn"
          @input-value="setModel"
          placeholder="Search symbol, eg. A"
          hide-bottom-space
          popup-content-style="background-color:#1A3F6A;color:white;max-height:150px"
          popup-content-class="searchPopup"
          @keydown.enter="directUser"
        >
          <template v-slot:prepend>
            <q-icon name="eva-search-outline" style="color: white" />
          </template>
          <template v-slot:no-option>
            <q-item>
              <q-item-section class="text-grey"> No results </q-item-section>
            </q-item>
          </template>
          <template v-slot:append>
            <q-icon
              style="color: #7e96b8"
              v-if="model !== null && model !== ''"
              class="cursor-pointer"
              name="clear"
              @click.stop="model = null"
            />
          </template>
        </q-select>
      </div>

      <div class="flex items-center q-gutter-x-lg">
        <q-tabs
          v-model="tab"
          style="color: #7e96b8"
          active-color="white"
          content-class="q-gutter-x-sm"
        >
        <q-route-tab name="sentient" label="Stock" exact to="/sentient" />
           <q-route-tab name="giro" label="Giro" exact to="/giro" />
          
         
          <!-- <q-route-tab name="Pricing" label="Page 3" exact to="" /> -->
        </q-tabs>

        <q-btn
          style="background: red; color: white"
          label="Log Out"
          icon="logout"
          rounded
          class="q-mr-xl q-py-xs"
          to="/login"
        />
      </div>
    </div>

    <!-- responsive for smaller than medium devices -->
    <div
      v-show="
        !this.$route.fullPath.includes('/login') &&
        !this.$route.fullPath.includes('/signup') &&
        !this.$route.fullPath.includes('/admin')
      "
      class="text-white flex justify-between items-center no-wrap lt-md"
      style="padding: 1vw 5vw"
    >
      <div class="flex items-center no-wrap">
        <div
          class="q-mr-xl"
          style="font-size: 35px; cursor: pointer"
          @click="$router.push('/home')"
        >
          <img
            src="statics/logo-white.png"
            alt=""
            style="width: 15vw; margin-top: 10px"
          />
        </div>

        <q-select
          dense
          behavior="menu"
          v-model="model"
          use-input
          hide-selected
          fill-input
          input-debounce="0"
          dropdown-icon="expand_more"
          input-style="color: white;"
          style="
            background-color: #1a3f6a;
            border-radius: 100px;
            width: 40vw;
            color: white;
          "
          class="myDropdown"
          rounded
          outlined
          :options="options"
          @filter="filterFn"
          @input-value="setModel"
          placeholder="Search symbol, eg. A"
          hide-bottom-space
          popup-content-style="background-color:#1A3F6A;color:white;max-height:150px"
          popup-content-class="searchPopup"
          @keydown.enter="directUser"
        >
          <template v-slot:prepend>
            <q-icon name="eva-search-outline" style="color: white" />
          </template>
          <template v-slot:no-option>
            <q-item>
              <q-item-section class="text-grey"> No results </q-item-section>
            </q-item>
          </template>
          <template v-slot:append>
            <q-icon
              style="color: #7e96b8"
              v-if="model !== null && model !== ''"
              class="cursor-pointer"
              name="clear"
              @click.stop="model = null"
            />
          </template>
        </q-select>
      </div>

      <q-btn flat @click="drawer = !drawer" round dense icon="menu" />
    </div>

    <q-drawer
      v-model="drawer"
      dark
      elevated
      mobile
      :width="250"
      :breakpoint="400"
      overlay
    >
      <q-scroll-area class="fit">
        <q-list padding>
          <q-item clickable v-ripple to="/home">
            <q-item-section avatar>
              <q-icon name="home" />
            </q-item-section>

            <q-item-section> Home </q-item-section>
          </q-item>

          <q-item clickable v-ripple to="/about">
            <q-item-section avatar>
              <q-icon name="info" />
            </q-item-section>

            <q-item-section> Giro</q-item-section>
          </q-item>

          <q-item clickable v-ripple to="/login" class="">
            <q-item-section avatar>
              <q-icon name="logout" />
            </q-item-section>

            <q-item-section> Log Out </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>

      <!-- <q-img class="absolute-top" src="https://cdn.quasar.dev/img/material.png" style="height: 150px">
          <div class="absolute-bottom bg-transparent">
            <q-avatar size="56px" class="q-mb-sm">
              <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
            <div class="text-weight-bold">Greg G Tan</div>
            <div>greggtan99@gmail.com</div>
          </div>
        </q-img> -->
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>

   
  </q-layout>
</template>

<script>
import EssentialLink from "components/EssentialLink.vue";
import router from "src/router";
import axios from "axios";
const linksList = [
  {
    title: "Docs",
    caption: "quasar.dev",
    icon: "school",
    link: "https://quasar.dev",
  },
  {
    title: "Github",
    caption: "github.com/quasarframework",
    icon: "code",
    link: "https://github.com/quasarframework",
  },
  {
    title: "Discord Chat Channel",
    caption: "chat.quasar.dev",
    icon: "chat",
    link: "https://chat.quasar.dev",
  },
  {
    title: "Forum",
    caption: "forum.quasar.dev",
    icon: "record_voice_over",
    link: "https://forum.quasar.dev",
  },
  {
    title: "Twitter",
    caption: "@quasarframework",
    icon: "rss_feed",
    link: "https://twitter.quasar.dev",
  },
  {
    title: "Facebook",
    caption: "@QuasarFramework",
    icon: "public",
    link: "https://facebook.quasar.dev",
  },
  {
    title: "Quasar Awesome",
    caption: "Community Quasar projects",
    icon: "favorite",
    link: "https://awesome.quasar.dev",
  },
];


// const stringOptions = [
// "NASDAQ:AAPL",
// "NYSE:A",
// "NYSE:AA",
// "NYSE:ABC",
// "NYSE:AMN",
// "NYSE:IBM",
// "NYSE:T",
// "NASDAQ:AMZN",
// "NASDAQ:GOOG",
// "NASDAQ:META",
// "NASDAQ:MSFT",
// "NASDAQ:NFLX",
// "NASDAQ:TSLA",
// "NASDAQ:TIGR",
// "NASDAQ:VOD",
// "NYSE:UBER",
// "OTC:YAHOY",
// "NASDAQ:AZN",
// "NASDAQ:DWAC",
// "NASDAQ:META",
// "NYSE:DIS",
// "NYSE:HRB"
// ]

export default {
  name: "MainLayout",

  components: {
    EssentialLink,
  },
  data() {
    return {
      options: [],
      optionsOriginal:[],
      model: "",
      drawer: false,
      tab: "sentient",
    };
  },
  methods: {
    filterFn(val, update, abort) {
      update(() => {
        const needle = val.toLocaleLowerCase();
        this.options = this.optionsOriginal.filter(
          (v) => v.toLocaleLowerCase().indexOf(needle) > -1
        );
      });
    },

    setModel(val) {
      this.model = val;
    },

    directUser() {
      // this.$store.commit("changeStockTicker", `NYSE:${this.model}`);
      this.$store.commit("changeStockTicker", `${this.model}`);
      this.$store.commit("changePureStockTicker", this.model);
      if (this.$router.currentRoute.path != "/stock/summary")
        this.$router.push(`/stock/summary`);
    },
  },
  async mounted() {
    let stockData = await axios.get('http://127.0.0.1:5000/api/stocks/getStocks')

    console.log('STOCK DATA', stockData.data)

    this.options = stockData.data
    this.optionsOriginal = stockData.data


    this.$router.push('/login')
  },
};
</script>

<style lang="scss">
.myDropdown i {
  color: white;
}

.searchPopup {
  max-height: 150px;
  height: auto !important;
  // height:400px;
  overflow: auto;
}
.searchPopup::-webkit-scrollbar {
  width: 5px;
}

.searchPopup::-webkit-scrollbar-track {
  border-radius: 5px;
}

.searchPopup::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: #7e96b8;
}

body::-webkit-scrollbar {
  width: 5px;
}

body::-webkit-scrollbar-track {
  // background: rgb(83, 109, 255);
  background-color: black;
  border-radius: 5px;
}

body::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: #445061;
}
</style>