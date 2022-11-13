<template>
    <q-page class="text-white flex justify-center items-center column" style="background:black">
      <div class="flex justify-center items-center column q-pa-lg" style="background:#1f1f1f;border-radius:15px;box-shadow: rgb(25,57,106) 0px 0px 30px;width:400px ">
        <div class="" style="font-size:30px">
          Enter Account Id
        </div>

        <q-input autofocus standout dark v-model="accountId" style="width:300px;font-size:20px" class="q-my-md"></q-input>

        <q-btn
            style="background: rgb(25,57,106); color: white;width:200px;"
            label="Log In"
            icon="logout"
            rounded
            flat
            :ripple="false"
            class=" q-py-xs q-mt-md loginButton"
            @click="loginUser()"
            
          />
      </div>
     
    </q-page>


</template>

<script>
import axios from "axios";

export default {
  methods: {
    async loginUser(){
      try{
        let loginRes = await axios.get(`http://127.0.0.1:5000/api/users/${this.accountId}/bankAccounts`)

        this.$store.state.giroAccountId = this.accountId
        this.$router.push('/sentient')
        this.$q.notify({
          type: "positive",
          icon: "done",
          message: `Giro Account ${this.accountId} Successfully Logged in`,
          timeout: 750,
        });

        

      }catch(err){
        console.log(err)
        this.$q.notify({
        type: "negative",
        icon: "error",
        message: `Invalid Giro Account Id!`,
        timeout: 750,
      });
      }
      
    }
  },
  data () {
    return {
      accountId:''
    }
  },
    
}
</script>


<style>
.loginButton{
  transition: 0.5s;
}

.loginButton:hover{
  transform: translateY(-3px);
  box-shadow: rgb(25,57,106) 0px 0px 30px;
}



</style>