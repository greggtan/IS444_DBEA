<template>
  
    <q-page >

      <div class="flex justify-center items-center column" style="height:90vh"  v-show="showPage == false">
        <q-spinner
        color="white"
        size="5em"
        />
        <div class="text-white q-mt-sm">Fetching Data...</div>
      </div>

      <div class="text-white q-pa-md q-mx-auto" style="max-width:1440px" v-show="showPage">
        <div class="flex justify-between items-center">
          <div class="" style="font-size:40px;font-weight:500">Giro Accounts</div>

          <div class="q-gutter-x-md">
            <q-btn
            style="background: rgb(25,57,106); color: white;"
            label="Add Billing Organization"
            icon="add"
            rounded
            flat
            :ripple="false"
            class=" q-py-xs q-mt-md loginButton"
            @click="addBillingOrgDialog = !addBillingOrgDialog"
            
          />
            <q-btn
            style="background: rgb(25,57,106); color: white;"
            label="Add Account"
            icon="add"
            rounded
            flat
            :ripple="false"
            class=" q-py-xs q-mt-md loginButton"
            @click="addAccountDialog = !addAccountDialog"
            
          />
          </div>
          
        </div>


        <!-- empty div -->
        <div class="text-center q-mt-lg" v-if="allAccountData.length == 0">
          <Lottie :options="defaultOptions" style="width:23vw" />
          <div class="font-700 font-size-28">No Giro Accounts Created Yet!</div>
          <div class="font-500 font-size-14 myTextGrey">Please add an account.</div>
        </div>

        <!-- not empty, show all -->
        <div class="" v-else>
          <div class="q-mt-md " v-for="(account,index) in allAccountData" :key="account.bankAccountID">
            <div class="" style="font-size:30px">Account {{index+1}}</div>
            <div class="loginButton q-mt-sm  no-wrap flex items-center justify-between" style="background: rgb(25,57,106);border-radius:15px;font-size:22px;cursor:pointer">
              <div class="q-mx-md">
                <Lottie :options="defaultOptions2"  style="height:150px" />
              </div>
              <div class="" style="width:80%">
                <div class="">Account Number: <b>{{account.bankAccountID}}</b></div>
                <div class="">Account Serving: 
                  <span v-if="account.billingOrganizations.length == 0">-</span>
                  <span v-else v-for="bank in account.billingOrganizations" :key="bank.accountID"><b>{{bank.billingOrgName}},  </b></span>

                </div>
              </div>


              <q-btn label="transaction history" no-wrap style="background:#64a1ff" class="q-mr-lg" @click="viewTransactionHistory(account.bankAccountID)"></q-btn>
              
            </div>

          </div>

        </div>
      </div>
     

        




        <q-dialog  v-model="addAccountDialog"   seamless >
          <q-card class="q-pa-md text-white" style="width:50vw" dark>
            <div class="text-center font-700" style="color:white; font-size:28px">Create Giro Account</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#3871c8; width:85px;height:2.5px"></div>

            
              <div class="q-mx-md">
                <div class="font-size-16 q-mb-xs">Username</div>
                <q-input  dark outlined v-model="username" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Username" style="font-size:16px" />
              </div>

              <div class="q-mx-md q-mt-md">
                <div class="font-size-16 q-mb-xs">PIN Number</div>
                <q-input  dark outlined v-model="pin" type="number" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a 6 Digit Pin Number" style="font-size:16px" />
              </div>
           
              <div class="q-mx-md q-mt-md">
                <div class="font-size-16 q-mb-xs">OTP</div>
                <div class="flex items-start justify-between no-wrap">
                  <q-input  dark outlined v-model="otp" type="number" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter OTP Sent Via SMS" style="font-size:16px; width:80%; " />
                  <q-btn label="Get OTP" color="red" class="" style="height:55px" @click="getOTP()"></q-btn>
                </div>
                
              </div>
           
              <div class="q-mx-md q-mt-md">
                <div class="font-size-16 q-mb-xs">Bank Account Number</div>
                <q-input  dark outlined v-model="bankAccountId" type="number" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter Bank Account Id" style="font-size:16px" />
              </div>
           
            

            <q-card-actions align="right" class="q-mt-sm">
              <q-btn flat label="Cancel" color="primary" v-close-popup />
              <q-btn  label="Create Giro Account" color="primary" @click="addBankAccount" />
            </q-card-actions>

           
            


            
          </q-card>
        </q-dialog>


        <q-dialog  v-model="addBillingOrgDialog"   seamless >
          <q-card class="q-pa-md text-white" style="width:50vw" dark>
            <div class="text-center font-700" style="color:white; font-size:28px">Giro Add Billing Organization</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#3871c8; width:85px;height:2.5px"></div>
              <div class="q-mx-md q-mt-md">
                <div class="font-size-16 q-mb-xs">Select a Bank Account</div>
                <q-select
                outlined
                v-model="bankAccountChosen"
                :options="bankAccountOptions"
                placeholder="Select a Bank Account"
                popup-content-class="selectPopup"
                dark
                use-input
                hide-selected
                fill-input
                input-debounce="0"
                hide-bottom-space
                
                style=""
                
              />
              </div>
              <div class="q-mx-md q-mt-md">
                <div class="font-size-16 q-mb-xs">Select a Billing Organization</div>
                <q-select
                outlined
                v-model="billingOrgChosen"
                :options="billingOrgsOptions"
                placeholder="Select a Billing Org"
                popup-content-class="selectPopup"
                dark
                use-input
                hide-selected
                fill-input
                input-debounce="0"
                hide-bottom-space
                @filter="filterFn"
                @input-value="setModel"
                style=""
                
              />
              </div>
             
           
              <!-- {{billingOrgs}} -->

            <q-card-actions align="right" class="q-mt-sm">
              <q-btn flat label="Cancel" color="primary" v-close-popup />
              <q-btn  label="Add Billing Organization" color="primary" @click="addBillingOrg()" />
            </q-card-actions>

           
            


            
          </q-card>
        </q-dialog>

        <q-dialog  v-model="transactionHistoryDialog"   seamless >
          <q-card class="q-pa-md text-white" style="max-width:80vw" dark>
            <div class="text-center font-700" style="color:white; font-size:24px">Transaction History - Bank Account {{currentBankAccount}}</div>
            
             
           <!-- add table here -->
           <q-table
          
            :data="data"
            :columns="columns"
            row-key="name"
            dark
            color="amber"
          />

            <q-card-actions align="right" class="q-mt-sm">
              <q-btn  label="close" color="primary" v-close-popup />
            </q-card-actions>

           
            


            
          </q-card>
        </q-dialog>

        


        
    </q-page>
</template>

<script>
import axios from "axios";
import Lottie from 'vue-lottie';
import * as animationData1 from './empty.json';
import * as animationData2 from './creditCard.json';
export default {
  components: {
    Lottie
  },
  methods: {
    async addBillingOrg(){
      console.log(this.bankAccountChosen, this.billingOrgChosen)

      let obj = this.billingOrgs.find(o => o.billingOrgName ==  this.billingOrgChosen)
      console.log('selected billing org object', String(Number(obj.accountID)))

      try{
        let addBillingOrgRes = await axios.post(`http://127.0.0.1:5000/api/users/${this.$store.state.giroAccountId}/billingOrganizations`,{
          bankAccountID:this.bankAccountChosen,
          billingOrganizationAccountID:String(Number(obj.accountID))
        })
        console.log('add billing org response', addBillingOrgRes.data)

        let getAccounts = await axios.get(`http://127.0.0.1:5000/api/users/${this.$store.state.giroAccountId}/bankAccounts`)
         this.allAccountData = getAccounts.data
        

        this.$q.notify({
          type: "positive",
          icon: "done",
          message: `${this.billingOrgChosen} Successfully Added To Bank Account ${this.bankAccountChosen}!`,
          timeout: 750,
        });

        this.addBillingOrgDialog = false //close dialog

        this.bankAccountChosen = '' 
        this.billingOrgChosen = ''


      }
      catch(err){
        console.log(err)
        this.$q.notify({
            type: "negative",
            icon: "error",
            message: `Billing Organization Already Added To A Bank Account! Please Choose Another.`,
            timeout: 750,
          });
      }

      

    },
    async addBankAccount(){
      if (this.username=='' || this.pin=='' || this.otp == '' || this.bankAccountId == ''){
        this.$q.notify({
          type: "negative",
          icon: "error",
          message: `Invalid Inputs, Please Try Again!`,
          timeout: 750,
        });
      }else{
      
        try{
          let addAccountRes = await axios.post(`http://127.0.0.1:5000/api/users/${this.$store.state.giroAccountId}/bankAccounts`,
        {
          userID:this.username,
          PIN:this.pin,
          OTP:this.otp,
          bankAccountID:this.bankAccountId,
        }
        )

        let getAccounts = await axios.get(`http://127.0.0.1:5000/api/users/${this.$store.state.giroAccountId}/bankAccounts`)
        this.allAccountData = getAccounts.data
        console.log(this.allAccountData)
        //to make the dropdown options for bank accounts
        let bankAccountOptions = []
        this.allAccountData.forEach(element => {
          bankAccountOptions.push(element.bankAccountID)
        });
        this.bankAccountOptions = bankAccountOptions
        

        this.addAccountDialog = false
        this.$q.notify({
          type: "positive",
          icon: "done",
          message: `Bank Account ${this.bankAccountId} Successfully Created!`,
          timeout: 750,
        });
      }
      catch(err){
        console.log(err)
        this.$q.notify({
            type: "negative",
            icon: "error",
            message: `Bank Account Creation Failed!`,
            timeout: 750,
          });
      }

       

        
      }
     
    },

    async resetHomePage(){
      let getAccounts = await axios.get(`http://127.0.0.1:5000/api/users/${this.$store.state.giroAccountId}/bankAccounts`)
      this.allAccountData = getAccounts.data
      console.log(this.allAccountData)
    },

    async viewTransactionHistory(bankAccount){
      // console.log(bankAccount)
      this.transactionHistoryDialog = true
      this.currentBankAccount = bankAccount
      let transactionHistory = await axios.get(`http://127.0.0.1:5000/api/users/${this.$store.state.giroAccountId}/bankAccounts/${bankAccount}/transactions`)

      console.log(transactionHistory.data)
      this.data = transactionHistory.data
    },

    async getOTP(){
      try{
        let otpRes = await axios.post(`http://127.0.0.1:5000/api/requestOTP/`, {
          userID:this.username,
          PIN:this.pin
        })



        this.$q.notify({
            type: "positive",
            icon: "done",
            message: `OTP Successfully Sent!`,
            timeout: 750,
          });
      }
      catch(err){
        console.log(err)
        this.$q.notify({
            type: "negative",
            icon: "error",
            message: `Please Enter Valid Username and PIN Number!`,
            timeout: 750,
          });
      }
     

    },
    filterFn(val, update, abort) {
      update(() => {
        const needle = val.toLocaleLowerCase();
        this.billingOrgsOptions = this.billingOrgsOptionsOriginal.filter(
          (v) => v.toLocaleLowerCase().indexOf(needle) > -1
        );
      });
    },

    setModel(val) {
      this.billingOrgChosen = val;
    },
    handleAnimation: function (anim) {
        this.anim = anim;
      },
  },
  data () {
    return {
      showPage:false,


      defaultOptions: {
        animationData: animationData1.default,
        loop:true,
        autoplay:true
      },
      defaultOptions2:{
        animationData: animationData2.default,
        loop:true,
        autoplay:true
      },

      allAccountData:[],

      addAccountDialog:false,
      username:'',
      pin:'',
      otp:'',
      bankAccountId:'',

      allbillingOrgs:[], //for the select dropdown
      addBillingOrgDialog:false,
      bankAccountOptions:[],
      bankAccountChosen:'',

      billingOrgChosen:'',
      billingOrgsOptions:[],




      transactionHistoryDialog:false,
      currentBankAccount:'',


      columns: [
        { name: 'date', label: 'Date', field: 'date',align: 'left', },
        { name: 'transactionAmount', label: 'Transaction Amount', field: 'transactionAmount',align: 'left', },
        { name: 'narrative', label: 'Narrative', field: 'narrative',align: 'left', },
        
        {
          name: 'GMSAccountID',
          required: true,
          label: 'GMS Account ID',
          align: 'left',
          field: 'GMSAccountID',
          sortable: true
        },
        { name: 'bankAccountID', align: 'left', label: 'Bank Account ID', field: 'bankAccountID', sortable: true },
        { name: 'billingOrganizationAccountID', label: 'Billing Org Account ID', field: 'billingOrganizationAccountID', align: 'left', sortable: true },
        
       
        { name: 'transactionReferenceNumber', label: 'Transaction Ref', field: 'transactionReferenceNumber', align: 'left', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) },
        { name: 'status', label: 'Status', field: 'status', align: 'left', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) }
      ],
      data: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          sodium: 87,
          calcium: '14%',
          iron: '1%'
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          sodium: 129,
          calcium: '8%',
          iron: '1%'
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          sodium: 337,
          calcium: '6%',
          iron: '7%'
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          sodium: 413,
          calcium: '3%',
          iron: '8%'
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          sodium: 327,
          calcium: '7%',
          iron: '16%'
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          sodium: 50,
          calcium: '0%',
          iron: '0%'
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          sodium: 38,
          calcium: '0%',
          iron: '2%'
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          sodium: 562,
          calcium: '0%',
          iron: '45%'
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          sodium: 326,
          calcium: '2%',
          iron: '22%'
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          sodium: 54,
          calcium: '12%',
          iron: '6%'
        }
      ]





    }
  },

  async mounted(){
    console.log(this.$store.state.giroAccountId)

    this.showPage = false


    let getAccounts = await axios.get(`http://127.0.0.1:5000/api/users/${this.$store.state.giroAccountId}/bankAccounts`)
    this.allAccountData = getAccounts.data
    console.log(this.allAccountData)
    //to make the dropdown options for bank accounts
    let bankAccountOptions = []
    this.allAccountData.forEach(element => {
      bankAccountOptions.push(element.bankAccountID)
    });
    this.bankAccountOptions = bankAccountOptions
    
    //to make dropdown options for billing orgs
    let getBillingOrgs = await axios.get(`http://127.0.0.1:5000/api/referenceData/billingOrganizations`)
    // console.log(getBillingOrgs.data)
    this.billingOrgs = getBillingOrgs.data

    let billingOrgsOptions = []
    getBillingOrgs.data.forEach(element => {
      billingOrgsOptions.push(element.billingOrgName)
    });

    this.billingOrgsOptions = billingOrgsOptions
    this.billingOrgsOptionsOriginal = billingOrgsOptions
    // console.log('dropdown options:', billingOrgsOptions)



    this.showPage = true
  }
    
}
</script>

<style lang="scss">
  .q-dialog
  {
    backdrop-filter: blur(3px);

    background:rgb(0,0,0,0.2);
  }

  .selectPopup {
  max-height: 250px;
  height: auto !important;
  // height:400px;
  overflow: auto;
}
.selectPopup::-webkit-scrollbar {
  width: 5px;
}

.selectPopup::-webkit-scrollbar-track {
  border-radius: 5px;
}

.selectPopup::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: #7e96b8;
}
  
</style>