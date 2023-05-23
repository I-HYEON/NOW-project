<!-- views/UpdateView.vue -->

<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit" value="수정">
    </form>
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
/* 스타일을 필요에 따라 추가 */
</style>