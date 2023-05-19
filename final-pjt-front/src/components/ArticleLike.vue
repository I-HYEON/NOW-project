<template>
    <div>
        좋아요 페이지
   <!-- <button @click="like">좋아요</button>
    {{article?.like_users.length}}
    {{article.id}} -->
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'ArticleLike',
    props:{
        article:Object
    },
    methods:{
        like(){
        }
    }

}
</script>

<style>

</style>