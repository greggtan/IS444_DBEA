<template>
  <q-page class=" ">
    <div class="q-mx-xl gt-sm">
      <div class="q-mt-sm q-gutter-x-lg flex justify-start " >
      <q-tabs
        v-model="tab"
        style="color: #7e96b8;"
        active-color="grey-2"
        active-bg-color="blue-grey-6"
        indicator-color="transparent"
        class=""
      >
        <q-route-tab
          name="summary"
          label="Summary"
          style="border-radius: 50px;padding:0px 20px"
          
          no-caps
          exact
          to="/stock/summary"
        />
        <q-route-tab name="charts" label="Charts" exact to="/stock/charts"  style="border-radius: 50px"
          class="q-px-lg"
          no-caps />
        <!-- <q-route-tab name="twitter" label="Twitter" exact to="/stock/twitter"  style="border-radius: 50px"
          class="q-px-lg"
          no-caps /> -->
        <!-- <q-route-tab
          name="financials"
          label="Financials"
          exact
           style="border-radius: 50px"
          class="q-px-lg"
          no-caps
          to="/stock/financials/incomeStatement"
        /> -->
      </q-tabs>
    </div>

    <q-page-container >
      <router-view />
    </q-page-container>
    </div>

    <div class="lt-md" style="margin-left:5vw; margin-right:5vw">
      <div class="q-mt-sm flex justify-start" >
      <q-tabs
        v-model="tab"
        style="color: #7e96b8"
        active-color="grey-2"
        active-bg-color="blue-grey-6"
        indicator-color="transparent"
        
      >
        <q-route-tab
          name="summary"
          label="Summary"
          style="border-radius: 50px;padding:0px 20px"
          
          no-caps
          exact
          to="/stock/summary"
        />
        <q-route-tab name="charts" label="Charts" exact to="/stock/charts"  style="border-radius: 50px"
          class="q-px-lg"
          no-caps />
        <!-- <q-route-tab name="twitter" label="Twitter" exact to="/stock/twitter"  style="border-radius: 50px"
          class="q-px-lg"
          no-caps /> -->
        <q-route-tab
          name="financials"
          label="Financials"
          exact
           style="border-radius: 50px"
          class="q-px-lg"
          no-caps
          to="/stock/financials/incomeStatement"
        />
      </q-tabs>
    </div>

    <q-page-container >
      <router-view />
    </q-page-container>
    </div>
    
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      tab: "summary",
    };
  },
  mounted(){
    this.$router.push('/stock/summary')
  }
};
</script>
