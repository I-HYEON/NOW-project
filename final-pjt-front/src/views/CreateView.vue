<!-- views/CreateView.vue -->

<template>
  <div class="create-container">
    <h1>게시글 작성</h1>
    <br>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="100" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/articles/`,
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        },

        data: { title, content},
        
      })
      .then(() => {
        // console.log(res)
        this.$router.push({name: 'article'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
.create-container {
  text-align:center;

}
</style>
