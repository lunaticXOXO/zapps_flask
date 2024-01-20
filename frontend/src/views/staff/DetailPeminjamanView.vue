<template>
    <v-app>
      <v-card 
          class="mt-10 text-center mx-10"
          max-width = "1450">
          <v-card
                  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
               Detail Peminjaman Buku
              </v-card-title>
        </v-card>
          <br>
        
          <v-data-table 
              :headers = "column"
              :items = "peminjaman">
             
          </v-data-table>
      </v-card>
      <br>
      
      
          <v-card class="mt-10 text-center mx-10" max-width="1450">
            <v-card
                  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
               Identitas Buku dan Peminjam
              </v-card-title>
        </v-card>
        <br>
            <v-data-table 
              :headers = "column2"
              :items = "detail_peminjaman">
          </v-data-table>
  
        </v-card>

        <v-card class = "mt-10 text-center mx-10" max-width="1450">
          <v-card
                  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
              Status Pengembalian Buku
              </v-card-title>
        </v-card>
          <br>
          <v-data-table 
              :headers = "column3"
              :items = "detail_peminjaman_return">
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
              {text : 'ID Peminjaman',          value : 'idborrow'},
              {text : 'Nama Peminjam',          value : 'nama_peminjam'},
              {text : 'Tanggal Pinjam',         value : 'tanggal_pinjam'},
              {text : 'Deadline',               value : 'deadline_pinjam'},
              {text : 'Jumlah Dipinjam',               value : 'quantity'},
                         
          ],
  
          column2 : [
            {text : 'User Id',                 value : 'userid'},
            {text : 'Username',                value : 'username'},
            {text : 'Email',                   value : 'email'},
            {text : 'ISBN',                    value : 'isbn'},
            {text : 'Book Name',               value : 'bookname'},
            {text : 'Penerbit',                value : 'penerbit'},
            {text : 'Price',                   value : 'price'},
            {text : 'Sisa Stock Quantity',     value : 'quantity'}
          ],
  
          column3 : [
              {text : 'ID Pengembalian'         , value : 'idreturn'},
              {text : 'Nama Pengembali'         , value : 'nama_pengembali'},
              {text : 'Tanggal Kembali'         , value : 'tanggal_kembali'},
              {text : 'Jumlah Pengembalian'     , value : 'quantity'},
              {text : 'IsReturn'                , value : 'isReturn'},
              {text : 'ID Peminjaman'           ,value : 'borrow'}
          ],
  
          
          peminjaman : [],
          detail_peminjaman : [],
          detail_peminjaman_return : [],
        
         
         
        }
      },
  
      mounted(){
          this.fetchPeminjamanById(),
          this.fetchDetailPeminjamanUsers(),
          this.fetchDetailBooksReturn()
      },
  
      methods: {
        
        async fetchPeminjamanById(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/list_borrow/' + this.$route.params.id);
            if (res.data == null){
             console.log("empty books")
            }else{
              this.peminjaman = res.data
              console.log(res,this.books)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
  
        async fetchDetailPeminjamanUsers(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/list_borrow_users/' + this.$route.params.id);
            if (res.data == null){
             console.log("empty book")
            }else{
              this.detail_peminjaman = res.data
              console.log(res,this.detail_peminjaman)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
  
        async fetchDetailBooksReturn(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/list_borrow_return/' + this.$route.params.id);
            if (res.data == null){
             console.log("empty book")
            }else{
              this.detail_peminjaman_return = res.data
              console.log(res,this.detail_peminjaman_return)
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