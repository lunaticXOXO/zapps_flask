<template>
    <v-card 
        class="mt-10 text-center mx-10"
        max-width = "1450">
        <br>
        <v-card
                color="#2596be"
                dark
                class="px-5 py-3"
                max-height ="200">
            <v-card-title class="text-h5">
             Daftar Buku Selesai Proses Peminjaman
            </v-card-title>
      </v-card>

        <v-data-table 
            :headers = "column"
            :items = "books">
           
        </v-data-table>
    </v-card>
</template>

<script>
import Login from "../../services/Login.js"
  export default {
    data(){
      return {
        valid : true,
        column : [
            {text : 'ISBN',              value : 'isbn'},
            {text : 'Book Name',         value : 'bookname'},
            {text : 'Nama Peminjam',     value : 'nama_peminjam'},
            {text : 'Tanggal Peminjaman', value : 'tanggal_pinjam'},
            {text : 'Batas Peminjaman',  value : 'deadline_pinjam'},
           {text : 'Quantity', value : 'quantity'},
        
           
        ],
        iduser : null,
        books : [],
        editedIndex: -1,
        loginService: new Login()
       
      }
    
    },

    mounted(){
        this.fetchBookReturnMember()
    },

    methods: {
      
        async fetchBookReturnMember() {
        try {
            const axios = require('axios');
            const res = await axios.get('/api/list_return_member/' + this.loginService.getID());

            if (!Array.isArray(res.data)) {
                console.error("Data is not an array:", res.data);
                return;
            }
            
            this.books = res.data;
            console.log(res, this.books);
        }
        catch (error) {
            alert("Error");
            console.log(error);
        }
    },

      
      
    }
  }
</script>