<!-- views/CreateView.vue -->

<template>
  <div class="create-container">
    <div class="create-form">
      <h1>게시글 작성</h1>
      <br>
      <form>
        <label for="title">제목</label>
        <br>
      
        <input type="text" placeholder="제목을 입력하세요" style="width: 600px;" id="title" v-model.trim="title"><br>
        <br>
        <label for="content">내용 </label>
        <br>
        <textarea id="content" placeholder="내용을 입력하세요" style="width: 600px;" rows="10" v-model="content"></textarea><br>
        <button type="button" @click="createArticle" style="width: 600px;" class="btn btn-success">글쓰기</button>
      </form>
    </div>
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
.create-container {
  text-align:center;

}
.half-width-form {
  width: 50%;
}
.create-form {
  display: inline-block;
  padding: 20px;
  width: 700px;
  height: 520px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
</style>
