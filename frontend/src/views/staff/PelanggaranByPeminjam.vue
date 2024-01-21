<template>
    <v-app>
      <v-card 
          class="mt-10 text-center mx-10"
          max-width = "1000">
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
      
      
          <v-card class="mt-10 text-center mx-10" max-width="1000">
            <v-card
                  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
               Informasi denda peminjaman {{this.$route.params.id}}
              </v-card-title>
        </v-card>
        <br>
            <v-data-table 
              :headers = "column2"
              :items = "violations">
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
              {text : 'Jumlah Dipinjam',         value : 'quantity'},
                         
          ],
  
          column2 : [
            {text : 'Violation Id',                 value : 'idviolation'},
            {text : 'Biaya Denda',  value : 'biaya_denda'},
            {text : 'Jumlah Pinjam', value : 'quantity_denda'},
            {text : 'Jenis Denda', value : 'description'}
           
          ],
  
        
          
          peminjaman : [],
         violations : [],
        
        
         
         
        }
      },
  
      mounted(){
          this.fetchPeminjamanById(),
          this.fetchPelanggaranByPeminjam()
        
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
              console.log(res,this.peminjaman)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
  
        async fetchPelanggaranByPeminjam(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/violation_peminjam/' + this.$route.params.id);
            if (res.data == null){
             console.log("empty book")
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
  
        
      }
    }
  </script>