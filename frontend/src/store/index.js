import Vue from 'vue'
import Vuex from 'vuex'

// import example from './module-example'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    // modules: {
    //   // example
    // },
    state: {
      accessToken:'',
      stockTicker:'NYSE:F',
      pureTicker:'',
      profilePicture:'',
      fullName:'',
      email:'',

      giroAccountId:''
    },
    getters:{
      getStockTicker: state =>{
        return state.stockTicker
      }
    },
    mutations: {
      changeStockTicker(state,newTicker){
        state.stockTicker = newTicker
        // console.log(newTicker, 'changed')
      },

      changePureStockTicker(state,newTicker){
        state.pureTicker = newTicker
        // console.log(newTicker, 'pure stock ticker changed')
      }
    },
    actions: {
      
    },
    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  })

  return Store
}
