<!-- views/UpdateView.vue -->

<template>
<div class="update-container">
    <div class="update-form">
      <h1>게시글 수정</h1>
      <br>
      <form @submit.prevent="updateArticle">
        <label for="title">제목</label>
        <br>
      
        <input type="text" id="title" style="width: 600px;" v-model.trim="title"><br>
        <br>
        <label for="content">내용 </label>
        <br>
        <textarea id="content"  style="width: 600px;" rows="10" v-model="content"></textarea><br>
        <button type="button" @click="updateArticle" style="width: 600px;" class="btn btn-success">글수정</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  
  created() {
    // 수정할 article 정보를 가져오는 API 호출
    // const articleId = this.$route.params.id
    axios.get(`${API_URL}/articles/${this.$route.params.id}/`)
      .then(response => {
        const article = response.data
        this.title = article.title
        this.content = article.content
      })
      .catch(error => {
        console.log(error)
      })
  },
  methods: {
    updateArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목을 입력해주세요.')
        return
      } else if (!content) {
        alert('내용을 입력해주세요.')
        return
      }

      axios({
        method: 'put',
        url: `${API_URL}/articles/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: { title, content },
      })
      .then(() => {
        this.$router.push({ name: 'article' })
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>

<style>
.update-container {
  text-align:center;

}
.update-form {
  display: inline-block;
  padding: 20px;
  width: 700px;
  height: 520px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
/* 스타일을 필요에 따라 추가 */
</style>