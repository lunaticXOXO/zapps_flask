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
             Daftar Buku
            </v-card-title>
      </v-card>
        <br>
      
        <v-data-table 
            :headers = "column"
            :items = "detail_returns">
           
        </v-data-table>
    </v-card>
    <br>
    
      <div class="d-flex">
        <v-card class="mt-10 text-center mx-10" max-width="700">
          <v-card
                color="#2596be"
                dark
                class="px-5 py-3"
                max-height ="200">
            <v-card-title class="text-h5">
             Daftar Buku Dipinjam
            </v-card-title>
      </v-card>
      <br>
          <v-data-table 
            :headers = "column2"
            :items = "detail_returns">
        </v-data-table>

      </v-card>
      <v-card class = "mt-10 ml-5" max-width="700">
        <v-card
                color="#2596be"
                dark
                class="px-5 py-3"
                max-height ="200">
            <v-card-title class="text-h5">
             Daftar Buku Kembali
            </v-card-title>
      </v-card>
        <br>
        <v-data-table 
            :headers = "column3"
            :items = "detail_returns">
        </v-data-table>

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
            {text : 'ISBN',              value : 'isbn'},
            {text : 'Book Name',         value : 'bookname'},
            {text : 'Author',            value : 'author'},
            {text : 'Penerbit',          value : 'penerbit'},
            {text : 'Category',          value : 'category'},
            {text : 'Quantity',          value : 'quantity'},
            {text : 'Price',             value : 'price'},
           
        ],

        column2 : [
          {text : 'ID Peminjaman',          value : 'idborrow'},
          {text : 'Nama Peminjam',          value : 'nama_peminjam'},
          {text : 'Tanggal Peminjaman',     value : 'tanggal_pinjam'},
          {text : 'Batas Peminjaman',        value : 'deadline_pinjam'},
          {text : 'IsBorrow',               value : 'isBorrow'}
        ],

        column3 : [
            {text : 'ID Pengembalian', value : 'idreturn'},
            {text : 'Nama Pengembali', value : 'nama_pengembali'},
            {text : 'Tanggal Kembali', value : 'tanggal_kembali'},
            {text : 'IsReturn'       , value : 'isReturn'},
            {text : 'ID Peminjaman'  ,value : 'borrow'}
        ],

        
      
        detail_returns : [],
       
       
       
      }
    },

    mounted(){
        this.fetchReturnBooksById()
       
    },

    methods: {
      
      async fetchReturnBooksById(){
        try{
          const axios = require('axios');
          const res = await axios.get('/api/detail_books_complete/' + this.$route.params.id);
          if (res.data == null){
           console.log("empty book")
          }else{
            this.detail_returns = res.data
            console.log(res,this.detail_returns)
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