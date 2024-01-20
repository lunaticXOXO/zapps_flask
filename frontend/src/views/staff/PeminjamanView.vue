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
               Daftar Buku Dipinjam
              </v-card-title>
        </v-card>
        
        <br>
          <v-data-table 
              :headers = "column"
              :items = "borrows">
              <template v-slot:[`item.idborrow`]="{ item }">
                <div v-if="item.idborrow === editedItem.idborrow">
                    <v-text-field disabled v-model="editedItem.idborrow" :hide-details="true" dense single-line :autofocus="true" v-if="item.idborrow == editedItem.idborrow"></v-text-field>
                    <span v-else>{{item.idborrow}}</span>
                </div>
                <div v-else>
                    <v-text-field v-model="editedItem.idborrow" :hide-details="true" dense single-line :autofocus="true" v-if="item.idborrow == editedItem.idborrow"></v-text-field>
                    <span v-else>{{item.idborrow}}</span>
                </div>
              </template>
              <template v-slot:[`item.bookname`]="{ item }">
                  <v-text-field v-model="editedItem.bookname" :hide-details="true" dense single-line v-if="item.idborrow == editedItem.idborrow" ></v-text-field>
                  <span v-else>{{item.bookname}}</span>
              </template>
              <template v-slot:[`item.nama_peminjam`]="{ item }">
                  <v-text-field v-model="editedItem.nama_peminjam" :hide-details="true" dense single-line v-if="item.idborrow == editedItem.idborrow" ></v-text-field>
                  <span v-else>{{item.nama_peminjam}}</span>
              </template>
              <template v-slot:[`item.tanggal_pinjam`]="{ item }">
                  <v-text-field v-model="editedItem.tanggal_pinjam" :hide-details="true" dense single-line v-if="item.idborrow == editedItem.idborrow" ></v-text-field>
                  <span v-else>{{item.tanggal_pinjam}}</span>
              </template>
  
              
              <template v-slot:[`item.deadline_pinjam`]="{ item }">

                 <!-- <v-text-field v-model="editedItem.deadline_pinjam" :hide-details="true" dense single-line v-if="item.idborrow == editedItem.idborrow" ></v-text-field>
                <span v-else>{{item.deadline_pinjam}}</span> -->
                                
                <v-text-field
                    v-model="editedItem.deadline_pinjam"
                    :hide-details="true"
                    dense
                    single-line
                    v-if="item.idborrow == editedItem.idborrow"
                    @click="openDatePicker"
                >
                    <v-date-picker
                        v-model="dateDialog"
                        @input="updateDeadline"
                    ></v-date-picker>
                </v-text-field>

                <span v-else>{{ item.deadline_pinjam }}</span>

              </template>
  
              <template v-slot:[`item.quantity`]="{ item }">
                  <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line v-if="item.idborrow == editedItem.idborrow" ></v-text-field>
                  <span v-else>{{item.quantity}}</span>
              </template>
  
  
              <template v-slot:[`item.aksi`]="{ item }">
                <div v-if="item.idborrow == editedItem.idborrow">
                    <v-icon color="red" class="mr-3" @click="close">
                    mdi-window-close
                    </v-icon>
                    <v-icon color="green"  @click="updatePeminjaman()">
                    mdi-content-save
                    </v-icon>
                </div>
  
                <div v-else>
                  <router-link :to="{name : 'ReturnBookByIdPinjam',params:{id : `${item.idborrow}`}}">
                  <v-btn class="mx-1" x-small color="green" @click="selectBooks(item)">
                      <v-icon small dark>mdi-check</v-icon>
                  </v-btn>
                  </router-link>

                  <router-link :to="{name : 'DetailPeminjamanStaff',params:{id : `${item.idborrow}`}}">
                  <v-btn class="mx-1" x-small color="blue" @click="selectBooks(item)">
                      <v-icon small dark>mdi-check</v-icon>
                  </v-btn>
                  </router-link>
              
  
                  <v-btn class="mx-1" x-small color="green" @click="editPeminjaman(item)">
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
        max-width = "1450">
       
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
            :headers = "column2"
            :items = "returns">
            <template v-slot:[`item.aksi`]="{ item }">
                <div v-if="item.idborrow == editedItem.idborrow">
                    <v-icon color="red" class="mr-3" @click="close">
                    mdi-window-close
                    </v-icon>
                    <v-icon color="green"  @click="updatePeminjaman()">
                    mdi-content-save
                    </v-icon>
                </div>
  
                <div v-else>
                  <router-link :to="{name : 'DetailPeminjamanStaff',params:{id : `${item.idborrow}`}}">
                  <v-btn class="mx-1" x-small color="blue" @click="selectBooks(item)">
                      <v-icon small dark>mdi-check</v-icon>
                  </v-btn>
                  </router-link>
              
  
                  <v-btn class="mx-1" x-small color="green" @click="editPeminjaman(item)">
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
        max-width="900">
        <br>
  
        <v-card
                  color="#2596be"
                  dark
                  class="px-5 py-3"
                  max-height ="200">
              <v-card-title class="text-h5">
              Pengajuan Peminjaman
              </v-card-title>
      </v-card>
  
  
      <v-form  class="pa-6"
          ref="form"
          v-model="valid"
          @submit.prevent="submitHandler"
          lazy-validation>
  
          <v-text-field
          class="mx-10"
          v-model="idborrow"
          label="ID Peminjaman"
          required
          ></v-text-field>

          <v-text-field
          class="mx-10"
          v-model="nama_peminjam"
          label="Nama Peminjam"
          required
          ></v-text-field>
  
          <v-menu     
              class="mt-6"
              transition="scale-transition"
              offset-y
              max-width="400px"
              min-width="400px"
            >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-7" :value="deadline_pinjam" v-bind="attrs" v-on="on" label="Batas Peminjaman" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            
            <v-date-picker full-width v-model="deadline_pinjam"></v-date-picker>
          </v-menu>

          <v-autocomplete
            class="mx-10"
            v-model="book_stock"
            :items="books"
            item-text="bookname"
            item-value="isbn"
            label="Daftar Buku">
        </v-autocomplete>

        <v-text-field
          class="mx-10"
          v-model="quantity"
          label="Jumlah dipinjam"
          required
          ></v-text-field>

          <v-autocomplete
            class="mx-10"
            v-model="users"
            :items="members"
            item-text="username"
            item-value="id"
            label="Members">
        </v-autocomplete>
  
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
              {text : 'Book Name',              value : 'bookname'},
              {text : 'Nama Peminjam',          value : 'nama_peminjam'},
              {text : 'Tanggal Pinjam',         value : 'tanggal_pinjam'},
              {text : 'Deadline',               value : 'deadline_pinjam'},
              {text : 'Jumlah Dipinjam',       value : 'quantity'},
              {text : 'Action',                value : 'aksi'},
             
          ],

          column2 : [
             {text : 'ID Peminjaman',          value : 'idborrow'},
              {text : 'Book Name',              value : 'bookname'},
              {text : 'Nama Peminjam',          value : 'nama_peminjam'},
              {text : 'Tanggal Pinjam',         value : 'tanggal_pinjam'},
              {text : 'Deadline',               value : 'deadline_pinjam'},
              {text : 'Jumlah Dipinjam',        value : 'quantity'},
              {text : 'Action',                 value : 'aksi'},
            
          ],
          borrows : [],
          books : [],
          members : [],
          returns : [],

          dateDialog: false,
  
            idborrow        : '',
            nama_peminjam   : '',
            deadline_pinjam : '',
            book_stock      : '',
            quantity        : undefined,
            users           : '',
          
          editedIndex: -1,
          editedItem: {
           
            idborrow        : '',
            nama_peminjam   : '',
            deadline_pinjam : '',
            book_stock      : '',
            quantity        : undefined,
            users           : '',
          },
          defaultItem: {
           
            idborrow        : '',
            nama_peminjam   : '',
            deadline_pinjam : '',
            book_stock      : '',
            quantity        : undefined,
            users           : '',
          },
  
        snackbar: {
          show: false,
          message: null,
          color: null
        },
  
        }
      },
  
      mounted(){
          this.fetchBorrows(),
          this.fetchBooks(),
          this.fetchReturn(),
          this.fetchMembers()
         
      },
  
      methods: {
        
    openDatePicker() {
        this.dateDialog = true;
    },
     updateDeadline(date) {
        this.editedItem.deadline_pinjam = date;
        this.dateDialog = false;
    },

      validate () {
          if(this.$refs.form.validate()){
            this.CreatePeminjaman()
          
          }
        },
  
        close () {
          setTimeout(() => {
              this.editedItem = Object.assign({}, this.defaultItem);
              this.editedIndex = -1;
          }, 300)
        },
  
        editPeminjaman(borrows){
          console.log('ID : ' + borrows.idborrow)
          this.editedIndex = this.borrows.indexOf(borrows);
          this.editedItem = Object.assign({}, borrows);
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

        async fetchReturn(){
          try{
            const axios = require('axios');
            const res = await axios.get('/api/is_return');
            if (res.data == null){
              
              console.log("empty")
  
            }else{
              this.returns = res.data
              console.log(res,this.returns)
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
  
        async CreatePeminjaman(){
          try{
            const axios = require('axios');
            const response = await axios.post('/api/borrow',
              { idborrow        : this.idborrow,
                nama_peminjam   : this.nama_peminjam,
                deadline_pinjam : this.deadline_pinjam,
                book_stock      : this.book_stock,
                quantity        : this.quantity,
                users           : this.users,
               
              }
            );
            console.log(response,this.data)
           if(response.data.status == "success"){
  
               this.snackbar = {
                message : "Pengaujuan pinjaman success",
                color : 'green',
                show : true
            }
  
            location.replace('/peminjamanStaff')
          }
            else if(response.data.status == "failed"){
                this.snackbar = {
                message : "Pengaujuan pinjaman gagal",
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