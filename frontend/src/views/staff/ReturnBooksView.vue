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
        
          return_books : [],
  
        
          
        
        snackbar: {
          show: false,
          message: null,
          color: null
        },
  
        }
      },
  
      mounted(){
          this.fetchReturnBooks()
        
      },
  
      methods: {
        
       
  
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
        
  
      }
    }
  
  </script>