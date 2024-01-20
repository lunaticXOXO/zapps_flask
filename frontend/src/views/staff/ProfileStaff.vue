<template>
    <v-app>
        <div class="d-flex">
            <v-card 
          class="mt-10 text-center mx-10"
          max-width = "1450">
          <v-card
                  color="#2596be"
                  dark
                 
                  max-height ="200">
              <v-card-title class="text-h5">
               Profile Staff
              </v-card-title>
        </v-card>
          <br>
        
          <v-data-table 
              :headers = "column"
              :items = "profile">
             
          </v-data-table>
      </v-card>
      <br>
        <v-card class="mt-10 text-center mx-10" max-width="1450">
            <v-card
                  color="#2596be"
                  dark
                 
                  max-height ="200">
              <v-card-title class="text-h5">
               Detail Staff
              </v-card-title>
        </v-card>
        <br>
            <v-data-table 
              :headers = "column2"
              :items = "detail_profiles">

            
          </v-data-table>
  
        </v-card>
        </div>
    
  </v-app>
  </template>
  
  <script>
  import Login from  "../../services/Login.js"
    export default {

      data(){
        return {
          valid : true,
          column : [
              {text : 'Username',              value : 'username'},
              {text : 'Email',                 value : 'email'},
            
             
          ],
  
          column2 : [
            {text : 'ID', value : 'id'},
            {text : 'Fullname',          value : 'fullname'},
            {text : 'Adress', value : 'adress'},
            {text : 'City' , value : 'city'},
            {text : 'Telephone', value : 'telephone'},
         
          ],
       
          
          profile : [],
          detail_profiles : [],
         LoginService : new Login()
     
         
        }
      },
  
      mounted(){
          this.BasicStaff(),
          this.DetailStaff()
         
      },
  
      methods: {
        
        async BasicStaff(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/staff_basic/' + this.LoginService.getID());
            if (res.data == null){
             console.log("empty users")
            }else{
              this.profile = res.data
              console.log(res,this.profile)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
  
        async DetailStaff(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/staff_logged/' + this.LoginService.getID());
            if (res.data == null){
             console.log("empty users")
            }else{
              this.detail_profiles = res.data
              console.log(res,this.detail_profiles)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
  
  
        
      }
    }
  </script>