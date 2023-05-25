<template>
  <div class="d-flex justify-content-center">
    <div class="container footer">
      <div class="row footer-content">
        <div class="col-2 footer-section about">
          <h6>About Us</h6>
          <p>서이현 방정우 신성환</p>
        </div>
        <div class="col-4 footer-section contact">
          <h6>Contact Us</h6>
          <div>Email: tjwn1408@gmail.com</div>
          <div>phone: 010-5558-6902</div>
        </div>
        <div class="col-6 footer-section links">
          <h6>Quick Links</h6>
          <div class="container row" style="list-style:none;">
            <div class="col"><a href="https://github.com/I-HYEON/1-Project/tree/main"><img src='@/photo/png/github.png' style="width:50px;"></a>team</div>
            <div class="col"><a href="https://github.com/I-HYEON"><img src='@/photo/png/github.png' style="width:50px;"></a>I-HYEON</div>
            <div class="col"><a href="https://github.com/balloooooon"><img src='@/photo/png/github.png' style="width:50px;"></a>balloooooon</div>
            <div class="col"><a href="https://github.com/hw2ny1"><img src='@/photo/png/github.png' style="width:50px;"></a>hw2ny1</div>
          </div>
        </div>
      </div>
      <div>
          <p>&copy; 2023 Your Company. All rights reserved.</p>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scope>

.footer {
  justify-content: center;
  align-items: center;
  text-align: center;
  color: white;
  margin: 10px 10px 10px 10px;
  padding-bottom: 0.3rem;
  padding-top: 0.3rem;
}

.footer-content {
  /* width: 80%; */
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  font-size: 0.6rem;
}

.stack_image {
  height: 10vh;
}
</style>