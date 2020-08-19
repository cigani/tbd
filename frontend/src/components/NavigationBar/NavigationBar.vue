<template>
  <v-navigation-drawer
    v-model="sidebar"
    app
    mini-variant>
    <v-list
      nav>
      <v-list-item
        v-for="item in menuItems"
        :key="item.title"
        :to="item.path">
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-content>{{ item.title }}</v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-menu>
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        icon
        v-bind="attrs"
        v-on="on"
      >
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </template>
    <v-list class="hidden-xs-only">
      <v-list-item
        color="primary"
        v-for="item in menuItems"
        :key="item.title"
        :to="item.path">
        <v-icon color="blue darn-2" left>{{ item.icon }}</v-icon>
        {{ item.title }}
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>

export default {
  name: "Navbar",
  props: {},
  data: () => ({
    sidebar: false,
    menuItems: [
      {title: 'Home', path: '/Users', icon: 'home'},
      {title: 'Sign Up', path: '/Create', icon: 'mdi-account'},
      {title: 'Sign In', path: '/auth', icon: 'lock_open'}
    ]
  }),
};
</script>
