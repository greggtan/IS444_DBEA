<template>
    <q-page style="background:black" class="flex justify-center items-center">
        <q-card class="q-pa-md text-white" style="width:45vw;border-radius:15px;box-shadow: rgb(25,57,106) 0px 0px 30px;" dark>
            <div class="text-center font-700" style="color:white; font-size:28px">Trading Session Creation</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#3871c8; width:85px;height:2.5px"></div>

              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">Start DateTime</div>
                <q-input dark outlined dense v-model="startDateTime" class="q-mb-md" placeholder="Click on the date and time icons to pick start date & time">
                  <template v-slot:prepend>
                    <q-icon name="event" class="cursor-pointer">
                      <q-popup-proxy transition-show="scale" transition-hide="scale">
                        <q-date v-model="startDateTime" mask="YYYY-MM-DD HH:mm">
                          <div class="row items-center justify-end">
                            <q-btn v-close-popup label="Close" color="primary" flat />
                          </div>
                        </q-date>
                      </q-popup-proxy>
                    </q-icon>
                  </template>

                  <template v-slot:append>
                    <q-icon name="access_time" class="cursor-pointer">
                      <q-popup-proxy transition-show="scale" transition-hide="scale">
                        <q-time v-model="startDateTime" mask="YYYY-MM-DD HH:mm" format24h>
                          <div class="row items-center justify-end">
                            <q-btn v-close-popup label="Close" color="primary" flat />
                          </div>
                        </q-time>
                      </q-popup-proxy>
                    </q-icon>
                  </template>
                </q-input>
              </div>

              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">Number Of Students:</div>
                <q-input dense    dark outlined v-model="numberOfStudents" type="number" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter Number Of Students" style="font-size:16px" />
              </div>
              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">Choose up to 5 stocks:</div>
                <q-select
                dark
                outlined
                v-model="stocks"
                multiple
                :options="options"
                counter
                dense
                max-values="5"
                hint="Max 5 selections"
                :rules="[val => !!val || 'Field is required']"
              />
              </div>
              
           
            

            <q-card-actions align="center" class="q-mt-sm">
              <q-btn :disable="!startDateTime || !numberOfStudents || !stocks"  label="Create Trading Session" color="primary" @click="createSession()" style="width:100%;font-size:16px" class="q-py-xs" />
            </q-card-actions>

           
          </q-card>

    </q-page>
</template>

<script>
import axios from "axios";
export default {
  methods: {
     async createSession(){
      console.log(this.startDateTime,this.numberOfStudents,this.stocks)

      this.stocks.forEach(async element => {
        let ticker = element.split(' ')[1].slice(1,-1)
   
        console.log(ticker)
        let stockPrice = await axios.get(`https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?region=SG&lang=en-SG&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=sg.finance.yahoo.com&.tsrc=finance`)

        console.log('TICKER:',ticker, 'STOCK PRICE:',stockPrice)
      });

      this.$q.notify({
        type: "positive",
        icon: "done",
        message: `Trading Session Created!`,
        timeout: 750,
        });

        // try{
        //     let reqPaymentRes = await axios.post(`http://127.0.0.1:5000/api/instructionManagement/newInstruction`,
        //     {
        //         GMSAccountID:this.payeeAccountID,
        //         billingOrganizationAccountID:this.billOrgAccountID,
        //         transactionAmount:this.transactionAmount,
        //         transactionReferenceNumber:this.transactionRefNo,
        //         narrative:this.narrative
        //     })
            
        //     console.log(reqPaymentRes.data)
        //     this.$q.notify({
        //     type: "positive",
        //     icon: "done",
        //     message: `Instruction Record Saved And Email Sent Successfully!`,
        //     timeout: 750,
        //     });
        // }
        // catch(err){
        //     console.log(err)
        //     this.$q.notify({
        //     type: "negative",
        //     icon: "error",
        //     message: `Instruction Creation Failed!`,
        //     timeout: 750,
        //   });
        // }
    }
  },
  data () {
    return {
        startDateTime:null,
        numberOfStudents:null,
        options: [
          'Google (GOOG)', 'Meta (META)', 'Telsa (TSLA)', 'Apple (APPL)', 'Microsoft (MSFT)',  'Amazon (AMZN)', 'Disney (DIS)'
        ],
        stocks:null,
      

    }
  },
   
}
</script>