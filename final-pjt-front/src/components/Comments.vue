<template>
  <div>
    <p v-if="isLogin">
      <h3>댓글 작성</h3>
      <!-- <input type="textarea" id="content" v-model="content" @keyup.enter="createComment"> -->
      <textarea id="content" placeholder="댓글을 입력하세요" style="width: 600px;" rows="5" v-model="content" @keyup.enter="createComment"></textarea>
      <br>
      <button type="button" id="content" @click="createComment" class="btn btn-outline-success">작성</button>
    </p>
    <br>
    <br>
    <template v-if="comments.filter(comment => comment.article === article.id).length === 0">
      <p>댓글이 없습니다.</p>
    </template>
    <template v-else="v-else">
      <div v-for="(comment, idx) in comments" :key="idx" v-if="comment.article === article.id">
        <div style="display: flex; align-items: center; justify-content: space-between;">
          <div>
            {{comment?.username}} : {{ comment?.content }}
            <hr>
          </div>
          <div>
            
            <p v-if="comment.username===userInfo.username">
              <template v-if="editingCommentId !== comment.id">
                <span @click="editComment(comment)">수정</span> |
                <span @click="deleteComment(comment)">삭제</span>
              </template>
              <template v-else>
                <input type="text" v-model="editedContent" @keyup.enter="updateComment(comment)">
                <button @click="updateComment(comment)">저장</button>
                <button @click="cancelEdit">취소</button>
              </template>
            </p>
          </div>
        </div>
      </div>
    </template>
    
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'Comments',
  data() {
    return {
      content: null,
      comments: this.$store.state.comments,
      editingCommentId: null,
      editedContent: ''
    };
  },
  props: {
    article: Object
  },
  computed: {
    isLogin() {
        return this.$store.getters.isLogin
    }
    ,
    userInfo() {
        return this.$store.state.userInfo
        }
  },
  created() {
    this.getComments();
  },
  methods: {
    deleteComment(comment) {
      axios({
        method: 'delete',
        url: `${API_URL}/articles/comments/${comment.id}/`
      })
        .then((response) => {
          console.log(response);
          this.getComments();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getComments() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/comments/`
      })
        .then((res) => {
          if (res.status === 404) {
            console.log('fdkfd');
          }
          this.comments = res.data;
        })
        .catch((err) => {
          this.comments = null;
        });
    },
    createComment() {
      const content = this.content;
      if (this.content) {
        axios({
          method: 'post',
          url: `${API_URL}/articles/${this.$route.params.id}/comments/`,
          data: { content },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then(() => {
            this.content = null;
            this.getComments();
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        alert('댓글을 입력하세요!');
      }
    },
    editComment(comment) {
      this.editingCommentId = comment.id;
      this.editedContent = comment.content;
    },
    updateComment(comment) {
      axios({
        method: 'put',
        url: `${API_URL}/articles/comments/${comment.id}/`,
        data: {
          content: this.editedContent
        }
      })
        .then(() => {
          this.editingCommentId = null;
          this.editedContent = '';
          this.getComments();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    cancelEdit() {
      this.editingCommentId = null;
      this.editedContent = '';
    },
    getArticles(){
      this.$store.state
    }
  }
};

</script>

<style>

</style>