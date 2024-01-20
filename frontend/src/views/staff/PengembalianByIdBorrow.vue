<template>
    <v-app>
        <div class="d-flex">
        <v-card 
          class="mt-10 text-center mx-10"
          max-width = "1100">
          <v-card
                  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
               Data Peminjaman {{this.$route.params.id}}
              </v-card-title>
        </v-card>
            <br>
            <v-data-table 
                :headers = "column"
                :items = "peminjaman">
            
            </v-data-table>
      </v-card>

        <v-card 
          class="mt-10 text-center mx-10"
          width = "800">
          
          <v-card
                  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
               Daftar Pengembalian Buku
              </v-card-title>
        </v-card>
        
        <br>
          <v-data-table 
              :headers = "column2"
              :items = "return_books">
            
          </v-data-table>
      </v-card>

        </div>
      
      <v-card
        class="mt-10 text-center mx-10"
        width="800">
        <br>
  
        <v-card  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
               Pengembalian Buku Peminjaman {{this.$route.params.id}}
              </v-card-title>
      </v-card>
  
  
      <v-form  class="pa-6"
          ref="form"
          v-model="valid"
          @submit.prevent="submitHandler"
          lazy-validation>
  
          <v-text-field
          class="mx-10"
          v-model="idreturn"
          label="ID Return"
          required
          ></v-text-field>
  
          <v-text-field
          class="mx-10"
          v-model="quantity"
          label="Quantity"
          ></v-text-field>
  
        
  
          <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              type="submit"
              @click="validate()">
                  Submit
          </v-btn>
      
          <v-btn
              color="error"
              class="mr-4"
              @click="reset">
                Reset
          </v-btn>
  
      </v-form>
      <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
        {{snackbar.message}}
      </v-snackbar>
    </v-card>
  </v-app>
  
  </template>
  
  <script>
    export default {
      data(){
        return {
          valid : true,
          column : [
              {text : 'ID Peminjaman',          value : 'idborrow'},
              {text : 'Nama Peminjam',          value : 'nama_peminjam'},
              {text : 'Tanggal Pinjam',         value : 'tanggal_pinjam'},
              {text : 'Deadline',               value : 'deadline_pinjam'},
              {text : 'Jumlah Dipinjam',               value : 'quantity'},
                         
          ],

          column2 : [
              {text : 'ID Pengembalian',         value : 'idreturn'},
              {text : 'Book Name',              value : 'bookname'},
              {text : 'Nama Pengembali',        value : 'nama_pengembali'},
          ],
  
          peminjaman : [],
          return_books : [],
  
            idreturn: '',
            quantity: '',
           
        
         
  
        snackbar: {
          show: false,
          message: null,
          color: null
        },
  
        }
      },
  
      mounted(){
          this.fetchPeminjamanById(),
          this.fetchReturnBooks()
         
      },
  
      methods: {

        validate () {
          if(this.$refs.form.validate()){
            this.CreateReturnByPeminjam()
          
          }
        },
        
        async fetchPeminjamanById(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/list_borrow/' + this.$route.params.id);
            if (res.data == null){
             console.log("empty books")
            }else{
              this.peminjaman = res.data
              console.log(res,this.peminjaman)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
        
        async fetchReturnBooks(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/list_returnbook');
            if (res.data == null){
              
              console.log("buku kosong")
  
            }else{
              this.return_books = res.data
              console.log(res,this.return_books)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
         
       
  
        async CreateReturnByPeminjam(){
          try{
            const axios = require('axios');
            const response = await axios.post('/api/create_return_peminjam/' + this.$route.params.id,
              { idreturn: this.idreturn,
                quantity: this.quantity,
               
               
              }
            );
            console.log(response,this.data)
           if(response.data.status == "success"){
  
               this.snackbar = {
                message : "Create return success",
                color : 'green',
                show : true
            }
  
            location.replace('/pengembalian/' + this.$route.params.id)
          }
            else if(response.data.status == "failed"){
                this.snackbar = {
                message : "Create return failed",
                color : 'red',
                show : true
            }}
            
          }
          catch(error){
            alert("Insert books error")
            console.log(error)
            this.snackbar = {
                message : "Insert books error",
                color : 'red',
                show : true}
            
          }
        },
  
        
  
      },
  
  
        
  
      
    }
  
  </script>