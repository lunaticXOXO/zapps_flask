<template>
    <v-app>
      <v-card 
          class="mt-10 text-center mx-10"
          max-width = "1200">
          
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
              :headers = "column"
              :items = "return_books">
             
            
              <template v-slot:[`item.aksi`]="{ item }">
               
  
                <div>
                  <router-link :to="{name : 'ListBooksDetailStaff',params:{id : `${item.idreturn}`}}">
                  <v-btn class="mx-1" x-small color="blue" @click="selectPengembalian(item)">
                      <v-icon small dark>mdi-check</v-icon>
                  </v-btn>
                  </router-link>
            
  
                </div>
              </template>
          </v-data-table>
      </v-card>
  
      <div class="d-flex">

     
      <v-card
        class="mt-10 text-center mx-10"
        width="800">
        <br>
  
        <v-card
                  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
               Pengajuan Pengembalian Buku
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
         
          ></v-text-field>


          <v-text-field
          class="mx-10"
          v-model="nama_pengembali"
          label="Nama Pengembali"
          ></v-text-field>
  
          <v-autocomplete
            class="mx-10"
            v-model="book_stock"
            :items="books"
            item-text="bookname"
            item-value="isbn"
            label="Daftar Buku">
        </v-autocomplete>

        <v-autocomplete
            class="mx-10"
            v-model="users"
            :items="members"
            item-text="username"
            item-value="id"
            label="Members">
        </v-autocomplete>

        <v-autocomplete
            class="mx-10"
            v-model="borrow"
            :items="borrows"
            item-text="nama_peminjam"
            item-value="idborrow"
            label="Peminjaman">
        </v-autocomplete>

        <v-text-field
          class="mx-10"
          v-model="quantity"
          label="Jumlah Pengembalian"
         
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
  
        <v-card
                  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
               Pengajuan Kehilangan / Kerusakan Buku
              </v-card-title>
      </v-card>
  
  
      <v-form  class="pa-6"
          ref="form"
          v-model="valid2"
          @submit.prevent="submitHandler"
          lazy-validation>
  
          <v-text-field
          v-model="isbn"
          label="ISBN"
          required
          ></v-text-field>
  
          <v-text-field
          v-model="bookname"
          label="Book Name"
          ></v-text-field>
  
          <v-text-field
          v-model="author"
          label="Author"
          ></v-text-field>
  
          <v-text-field
          v-model="penerbit"
          label="Penerbit"
          ></v-text-field>
  
          <v-text-field
          v-model="category"
          label="Category"
          ></v-text-field>
  
          <v-text-field
          v-model="quantity"
          label="Quantity"
          ></v-text-field>
  
          <v-text-field
          v-model="price"
          label="Price"
          ></v-text-field>
  
          <v-btn
              :disabled="!valid2"
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
              {text : 'ID Pengembalian',         value : 'idreturn'},
              {text : 'Book Name',              value : 'bookname'},
              {text : 'Nama Pengembali',        value : 'nama_pengembali'},
              {text : 'Jumlah Kembali',         value : 'quantity'},
              {text : 'Tanggal Kembali',        value : 'tanggal_kembali'},
              {text : 'Action',                 value : 'aksi'},
  
             
          ],
        
          borrows : [],
          books : [],
          members : [],
  
            idreturn        : '',
            nama_pengembali: '',
            book_stock     : '',
            users: '',
            borrow : '',
            quantity: '',
           
          
        
        snackbar: {
          show: false,
          message: null,
          color: null
        },
  
        }
      },
  
      mounted(){
          this.fetchReturnBooks(),
          this.fetchBooks(),
          this.fetchMembers(),
          this.fetchBorrows()
         
      },
  
      methods: {
        
        validate () {
          if(this.$refs.form.validate()){
            this.CreateReturn()
          
          }
        },

        validate2 () {
          if(this.$refs.form.validate()){
            this.CreateViolation
          
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
        
        async fetchBooks(){
        try{
          const axios = require('axios');
          const res = await axios.get('/api/getbooks');
          if (res.data == null){
           console.log("empty book")
          }else{
            this.books = res.data
            console.log(res,this.books)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

      async fetchMembers(){
        try{
          const axios = require('axios');
          const res = await axios.get('/api/show_members');
          if (res.data == null){
           console.log("empty members")
          }else{
            this.members = res.data
            console.log(res,this.members)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },
      
      async fetchBorrows(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/is_borrow');
            if (res.data == null){
              
              console.log("empty")
  
            }else{
              this.borrows = res.data
              console.log(res,this.borrows)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },

  
        async CreateReturn(){
          try{
            const axios = require('axios');
            const response = await axios.post('/api/create_return',
              { idreturn: this.idreturn,
                nama_pengembali: this.nama_pengembali,
                book_stock: this.book_stock,
                users: this.users,
                borrow: this.borrow,
                quantity: this.quantity,
               
              }
            );
            console.log(response,this.data)
           if(response.data.status == "success"){
  
               this.snackbar = {
                message : "Create pengembalian Success",
                color : 'green',
                show : true
            }
  
            location.replace('/returnBooksView')
          }
            else if(response.data.status == "failed"){
                this.snackbar = {
                message : "Create pengembalian failed",
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