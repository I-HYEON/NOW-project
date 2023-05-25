<template>
  <div class="container footer">
    <div class="row">
      <div class="col">
        <nav>
        <a href='https://github.com/I-HYEON/1-Project' target='_blank'>Github</a>
        </nav>
        <p>
            <span>저자 : 갓이현 갓이현 갓이현</span><br/>
            <span>이메일 : 갓이현@gmail.com</span><br/>
            <span>Copyright 2023. All Rights Reserved.</span><br>
        </p>
      </div>
      <div class="col">
        <img class="stack_image" src="@/photo/stack/django.png" alt="django.png">
        <img class="stack_image" src="@/photo/stack/vue.png" alt="vue.png">
        <img class="stack_image" src="@/photo/stack/html css js.png" alt="html,css,js.png">
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style>
.footer {
  padding-bottom: 0.3rem;
  padding-top: 0.3rem;
}

.stack_image {
  height: 10vh;
}
</style>