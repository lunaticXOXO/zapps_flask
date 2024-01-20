<template>
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
            :items = "books">
           
        </v-data-table>
    </v-card>
</template>

<script>
  export default {
    data(){
      return {
        valid : true,
        column : [
            {text : 'ISBN',         value : 'isbn'},
            {text : 'Book Name',    value : 'bookname'},
            {text : 'Author',       value : 'author'},
            {text : 'Penerbit',     value : 'penerbit'},
            {text : 'Category',      value : 'category'},
            {text : 'Quantity',      value : 'quantity'},
            {text : 'Price',         value : 'price'},
           
        ],
        books : [],
        editedIndex: -1,
       
       
      }
    },

    mounted(){
        this.fetchBooks()
    },

    methods: {
      
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

      
      
    }
  }
</script>