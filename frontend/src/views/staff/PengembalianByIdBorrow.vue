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
      
      <div class="d-flex">
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

    <v-card
        class="mt-10 text-center mx-10"
        width="800">
        <br>
  
        <v-card  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
               Pengajuan Kehilangan / Kerusakan Peminjaman {{this.$route.params.id}}
              </v-card-title>
      </v-card>
      <v-form  class="pa-6"
          ref="form2"
          v-model="valid2"
          @submit.prevent="submitHandler"
          lazy-validation>
  
          <v-autocomplete
            class="mx-10"
            v-model="violation_type"
            :items="violations"
            item-text="description"
            item-value="id"
            label="Jenis Pelanggaran">
        </v-autocomplete>

        <v-autocomplete
            class="mx-10"
            v-model="damaged_level"
            :items="damages"
            item-text="description"
            item-value="id"
            label="Tingkat Kerusakan">
        </v-autocomplete>
  
          <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              type="submit"
              @click="validate2()">
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

      </div>

    


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
          violations : [],
          damages : [],
  
            idreturn: '',
            quantity: '',
           violation_type : undefined,
           damaged_level : undefined,
        
         
  
        snackbar: {
          show: false,
          message: null,
          color: null
        },
  
        }
      },
  
      mounted(){
          this.fetchPeminjamanById(),
          this.fetchReturnBooks(),
          this.fetchViolationType(),
          this.fetchDamageLevel()
         
      },
  
      methods: {

        validate () {
          if(this.$refs.form.validate()){
            this.CreateReturnByPeminjam()
          
          }
        },

        validate2 () {
          if(this.$refs.form2.validate()){
            this.CreateViolationByPeminjam()
          
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

        async fetchViolationType(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/damage_level');
            if (res.data == null){
              
              console.log("empty")
            }else{
              this.damages = res.data
              console.log(res,this.damages)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },

        async fetchDamageLevel(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/violation_type');
            if (res.data == null){
              
              console.log("empty")
            }else{
              this.violations = res.data
              console.log(res,this.violations)
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
            if(response.data.denda == "False"){
              location.replace('/pengembalian/' + this.$route.params.id)

            }else if(response.data.denda == "True"){
              location.replace('/violationPeminjam/' + this.$route.params.id)
            }
           
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
  
        async CreateViolationByPeminjam(){

          try{
            const axios = require('axios');
            const response = await axios.post('/api/create_violation_peminjam/' + this.$route.params.id,
              { violation_type: this.violation_type,
                damaged_level: this.damaged_level,
               
              }
            );
            console.log(response,this.data)
           if(response.data.status == "success"){
  
               this.snackbar = {
                message : "Create return success",
                color : 'green',
                show : true
            }
            location.replace('/violationPeminjam/' + this.$route.params.id)
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

        }
  
      },  
      
    }
  
  </script>