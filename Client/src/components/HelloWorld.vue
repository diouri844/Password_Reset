<template>
  <div>
      <h1> Reste Users Passwords </h1>
      <div class="form-container">
        <textarea rows="10" cols="3"  
        v-model="emailList"
        class="text_email_area"/>
        <button class="btn"
        @click="CheckEmailList"
        > Reset </button>
      </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data(){
    return{
      'emailList':''
    }
  },
  methods:{
    CheckEmailList(){
      console.log(
        this.emailList
        );
        // cast to array :
        let email_array = [];
        this.emailList.split("\n").forEach(
          ( email_item )=>{
            if ( this.ValidateEmail(email_item)){
              email_array.push(email_item);
            }
          }
        );
        console.log(
          email_array
        );
      let dataToSend = new FormData();
      dataToSend.append('emailList', email_array)
        axios.post('http://127.0.0.1:5000/Reset',
          dataToSend
      )
      .then( response => {
        console.log(response.data.ResponseData);
        
      })
      .catch( error => console.error(error));
        return;
    },
    ValidateEmail(email) {
      var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
      return email.match(validRegex)
      }

  }
}


</script>

<style>
.form-container{
  display: grid;
  grid-column: 1;
}
.text_email_area{
  padding: 10px;
}
.btn{
  margin-top:5%;
  width: 100%;
}
</style>