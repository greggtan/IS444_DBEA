<template>
    <q-page style="background:black" class="flex justify-center items-center">
        <q-card class="q-pa-md text-white" style="width:40vw" dark>
            <div class="text-center font-700" style="color:white; font-size:28px">Bill Organization Request Payment</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#3871c8; width:85px;height:2.5px"></div>

            
              
           
          
           
              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">BillOrg AccountID</div>
                <q-input  dense   dark outlined v-model="billOrgAccountID" type="number" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter Bill Organization Id" style="font-size:16px" />
              </div>
              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">Payee AccountID</div>
                <q-input dense    dark outlined v-model="payeeAccountID" type="number" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter Payee Account Id" style="font-size:16px" />
              </div>
              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">Transaction Amount</div>
                <q-input dense    dark outlined v-model="transactionAmount" type="number" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter Transaction Amount" style="font-size:16px" />
              </div>
              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">Transaction Ref No.</div>
                <q-input dense    dark outlined v-model="transactionRefNo" type="number" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter Transaction Ref No." style="font-size:16px" />
              </div>
              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">Narrative</div>
                <q-input  dense   dark outlined v-model="narrative"  :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter Narrative" style="font-size:16px" />
              </div>
           
            

            <q-card-actions align="center" class="q-mt-sm">
              <q-btn  label="Request Payment" color="primary" @click="requestPayment()" style="width:100%;font-size:16px" class="q-py-xs" />
            </q-card-actions>

           
            


            
          </q-card>

    </q-page>
</template>

<script>
import axios from "axios";
export default {
  methods: {
    async requestPayment(){

        try{
            let reqPaymentRes = await axios.post(`http://127.0.0.1:5000/api/instructionManagement/newInstruction`,
            {
                GMSAccountID:this.payeeAccountID,
                billingOrganizationAccountID:this.billOrgAccountID,
                transactionAmount:this.transactionAmount,
                transactionReferenceNumber:this.transactionRefNo,
                narrative:this.narrative
            })
            
            console.log(reqPaymentRes.data)
            this.$q.notify({
            type: "positive",
            icon: "done",
            message: `Instruction Record Saved And Email Sent Successfully!`,
            timeout: 750,
            });
        }
        catch(err){
            console.log(err)
            this.$q.notify({
            type: "negative",
            icon: "error",
            message: `Instruction Creation Failed!`,
            timeout: 750,
          });
        }
        



    }
  },
  data () {
    return {
        
        billOrgAccountID:'',
        payeeAccountID:'',
        transactionAmount:'',
        transactionRefNo:'',
        narrative:'',

    }
  },
   
}
</script>