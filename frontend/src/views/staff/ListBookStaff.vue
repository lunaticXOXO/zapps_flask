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
             Daftar Buku Staff
            </v-card-title>
      </v-card>
      
      <br>
     

        <v-data-table 
            :headers = "column"
            :items = "books">
            <template v-slot:[`item.isbn`]="{ item }">
              <div v-if="item.isbn === editedItem.isbn">
                  <v-text-field disabled v-model="editedItem.isbn" :hide-details="true" dense single-line :autofocus="true" v-if="item.isbn == editedItem.isbn"></v-text-field>
                  <span v-else>{{item.isbn}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.isbn" :hide-details="true" dense single-line :autofocus="true" v-if="item.isbn == editedItem.isbn"></v-text-field>
                  <span v-else>{{item.isbn}}</span>
              </div>
            </template>
            <template v-slot:[`item.bookname`]="{ item }">
                <v-text-field v-model="editedItem.bookname" :hide-details="true" dense single-line v-if="item.isbn == editedItem.isbn" ></v-text-field>
                <span v-else>{{item.bookname}}</span>
            </template>
            <template v-slot:[`item.author`]="{ item }">
                <v-text-field v-model="editedItem.author" :hide-details="true" dense single-line v-if="item.isbn == editedItem.isbn" ></v-text-field>
                <span v-else>{{item.author}}</span>
            </template>
            <template v-slot:[`item.penerbit`]="{ item }">
                <v-text-field v-model="editedItem.penerbit" :hide-details="true" dense single-line v-if="item.isbn == editedItem.isbn" ></v-text-field>
                <span v-else>{{item.penerbit}}</span>
            </template>

            
            <template v-slot:[`item.category`]="{ item }">
                <v-text-field v-model="editedItem.category" :hide-details="true" dense single-line v-if="item.isbn == editedItem.isbn" ></v-text-field>
                <span v-else>{{item.category}}</span>
            </template>

            <template v-slot:[`item.quantity`]="{ item }">
                <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line v-if="item.isbn == editedItem.isbn" ></v-text-field>
                <span v-else>{{item.quantity}}</span>
            </template>

            <template v-slot:[`item.price`]="{ item }">
                <v-text-field v-model="editedItem.price" :hide-details="true" dense single-line v-if="item.isbn == editedItem.isbn" ></v-text-field>
                <span v-else>{{item.price}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.isbn == editedItem.isbn">
                  <v-icon color="red" class="mr-3" @click="close">
                  mdi-window-close
                  </v-icon>
                  <v-icon color="green"  @click="updateBooks()">
                  mdi-content-save
                  </v-icon>
              </div>

              <div v-else>
                <router-link :to="{name : 'ListBooksDetailStaff',params:{id : `${item.isbn}`}}">
                <v-btn class="mx-1" x-small color="blue" @click="selectBooks(item)">
                    <v-icon small dark>mdi-check</v-icon>
                </v-btn>
                </router-link>
            

                <v-btn class="mx-1" x-small color="green" @click="editBuku(item)">
                    <v-icon small dark>mdi-pencil</v-icon>
                </v-btn>
                  
                <v-btn class="mx-1" x-small color="red" @click="deleteBooks(item)">
                    <v-icon small dark>mdi-trash-can-outline</v-icon>
                </v-btn>

              </div>
            </template>
        </v-data-table>
    </v-card>

    <v-card
      class="mt-10 text-center mx-10"
      max-width="1100">
      <br>

      <v-card
                color="#2596be"
                dark
                class="px-5 py-3"
                max-height ="200">
            <v-card-title class="text-h5">
             Tambah Daftar Buku
            </v-card-title>
    </v-card>


    <v-form  class="pa-6"
        ref="form"
        v-model="valid"
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
            {text : 'ISBN',            value : 'isbn'},
            {text : 'Book Name',       value : 'bookname'},
            {text : 'Author',           value : 'author'},
            {text : 'Penerbit',          value : 'penerbit'},
            {text : 'Category',           value : 'category'},
            {text : 'Quantity',           value : 'quantity'},
            {text : 'Price',           value : 'price'},
            {text : 'Action',           value : 'aksi'},

           
        ],
        books : [],

          isbn: '',
          bookname: '',
          author: '',
          penerbit: '',
          category: '',
          quantity: '',
          price: '',
        
        editedIndex: -1,
        editedItem: {
          isbn: '',
          bookname: '',
          author: '',
          penerbit: '',
          category: '',
          quantity: '',
          price: '',
        },
        defaultItem: {
          isbn: '',
          bookname: '',
          author: '',
          penerbit: '',
          category: '',
          quantity: '',
          price: '',
        },

      snackbar: {
        show: false,
        message: null,
        color: null
      },

      }
    },

    mounted(){
        this.fetchBooks()
       
    },

    methods: {
      
      validate () {
        if(this.$refs.form.validate()){
          this.AddBooks()
        
        }
      },

      close () {
        setTimeout(() => {
            this.editedItem = Object.assign({}, this.defaultItem);
            this.editedIndex = -1;
        }, 300)
      },

      editBuku(books){
        console.log('ID : ' + books.isbn)
        this.editedIndex = this.books.indexOf(books);
        this.editedItem = Object.assign({}, books);
      },

      async deleteBooks(books){
          console.log('ID : ' + books.isbn)
         
          const axios = require('axios');
          const response = await axios.delete(`/api/delete_book/${books.isbn}`);

          if(response.data.status == 'success'){
              console.log("delete success")
          }
          location.replace('/listBukuStaff') 
       
      
      },

      async fetchBooks(){
        try{
          const axios = require('axios');
          const res = await axios.get('/api/getbooks');
          if (res.data == null){
            
            console.log("buku kosong")

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

       
      selectBooks(books){
          console.log('ID : ' + books.isbn)
         
      },

      async AddBooks(){
        try{
          const axios = require('axios');
          const response = await axios.post('/api/books',
            { isbn: this.isbn,
              bookname: this.bookname,
              author: this.author,
              penerbit: this.penerbit,
              category: this.category,
              quantity: this.quantity,
              price: this.price,
             
            }
          );
          console.log(response,this.data)
         if(response.data.status == "success"){

             this.snackbar = {
              message : "Insert books Success",
              color : 'green',
              show : true
          }

          location.replace('/listBukuStaff')
        }
          else if(response.data.status == "failed"){
              this.snackbar = {
              message : "Insert books failed",
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

        async updateBooks(){
        if (this.editedIndex > -1) {
            Object.assign(this.books[this.editedIndex], this.editedItem)
            console.log(this.editedItem)
        }
        this.close()
        try{
            const axios = require('axios')
            const res = await axios.post('/api/update_book/'+ this.editedItem.isbn,
            { isbn: this.editedItem.isbn,
              bookname: this.editedItem.bookname,
              author: this.editedItem.author,
              penerbit: this.editedItem.penerbit,
              category: this.editedItem.category,
              quantity: this.editedItem.quantity,
              price: this.editedItem.price,
              
            
            })
            console.log(res)
        }catch(error){
            console.log(error)
        }
      } 
    

    },


      

    
  }

</script>