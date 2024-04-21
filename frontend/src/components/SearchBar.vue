<template>
   <div class="input-group input-group-lg" id="searchBar">
        <span class="input-group-text" id="addon-wrapping"><i class="bi bi-search" id="search"></i></span>
        <input type="text" @input="UserType" class="form-control" placeholder="Search" aria-describedby="inputGroup-sizing-lg">
    </div>
</template>

<script>
export default {
    emits:['search-query'],
    setup(props,{emit}){

        const UserType = (event) => {
            emit('search', event.target.value);
        };

        return{
            UserType,
        };
    }

}
</script>

<style scoped>
#search{
    font-size: 20px;
}

#searchBar{
    box-shadow: 5px 7px 8px 0px rgba(180, 180, 180, 0.5);
    border-radius: 20px;
    border: 1px solid rgba(180, 180, 180, 0.5);
    top: 20px;
    border: none;
    width: 90%;
    margin: 0 auto;
    height: 60px;
}

.input-group-text, .form-control{
    border: none;
    /* border-radius: 20px 0 0 20px; */
}

</style>