return {
  {
    "sindrets/diffview.nvim",
    dependencies = {
      { "nvim-tree/nvim-web-devicons", lazy = true },
    },
  },
  {
    "NeogitOrg/neogit",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "sindrets/diffview.nvim",
      "nvim-telescope/telescope.nvim",
    },
    config = function()
      require('neogit').setup({
        integrations = {
          telescope = true,
          diffview = true,
        }
      })
    end,
    keys = {
      vim.keymap.set('n', '<leader>gg', ":Neogit kind=floating<CR>"),
      vim.keymap.set('n', '<leader>ggd', ":Neogit cwd=")
    },
  },
  {
    "lewis6991/gitsigns.nvim",
    config = function()
      require('gitsigns').setup()

      vim.keymap.set("n", "<leader>gp", ":Gitsigns preview_hunk<CR>", {})
    end
  }
}
