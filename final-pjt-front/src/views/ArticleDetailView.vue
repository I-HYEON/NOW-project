<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="deleteArticle">삭제</button>
    <br><br><br>
      <h3>댓글 작성</h3>
    <form @submit.prevent="createComment">
      <label for="content">내용 : </label>
      <input type="text" id="content" v-model="content" @keyup.enter="getComments">
      <!-- <textarea id="content" cols="10" rows="10" v-model="content"></textarea><br> -->
      <input type="submit" @click="getComments">
    </form>
<br>
      <template v-if="comments.length === 0">
      <p>댓글이 없습니다.</p>
    </template>
    <template v-else>
      <p v-for="(comment, idx) in comments" :key="idx" v-if="comment.article === article?.id">
        댓글: {{ comment?.content }}
        <button @click="deleteComment(comment)">삭제</button>
      </p>
    </template>
    
  
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article: null,
      content: null,
    }
  },
  computed:{
    comments(){
      return this.$store.state.comments
    }
  },
  created() {
    this.getArticleDetail()
    this.getComments()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${ this.$route.params.id }/`,
      })
      .then((res) => {
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getComments(){
      // axios({
      //   method: 'get',
      //   url:`${API_URL}/articles/comments/`,
      // })
      // .then((res)=>{
      //   console.log(res)
      //   this.comments = res.data
      // })
      // .catch((err)=>console.log(err))
      this.$store.dispatch('getComments')
    },
    createComment(){
      const content = this.content
      if (this.content)
      axios({
        method:'post',
        url: `${API_URL}/articles/${ this.$route.params.id }/comments/`,
        data: {content},
      })
      .then(()=> {
        this.content=null
        
      })
      else{
        alert('댓글을 입력하세요!')
      }
    },
    deleteComment(comment) {
  axios({
    method: 'delete',
    url: `${API_URL}/articles/comments/${comment.id}/`,
  })
    .then(() => {
      this.getComments()
      // if (this.comments.length === 1) {
      //   // 댓글이 마지막 하나인 경우 페이지 새로고침
      //   location.reload();
      // }
    })
    .catch((err) => {
      console.log(err);
      
    });
    },
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/articles/${ this.$route.params.id }`
      })
      .then(()=>{
        this.$router.push({ path: '/article' });
      })
    }
    },
  }

</script>
