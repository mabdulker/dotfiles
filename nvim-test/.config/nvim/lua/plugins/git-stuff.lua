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
    keys = {
      {'<leader>gg', ":Neogit kind=floating<CR>", desc = "Open Neogit"},
      {'<leader>ggd', ":Neogit cwd=", desc = "Open Neogit in dir"}
    },
    config = function()
      require('neogit').setup({
        integrations = {
          telescope = true,
          diffview = true,
        }
      })
    end
  },
  {
    "lewis6991/gitsigns.nvim",
    config = function()
      require('gitsigns').setup()

      vim.keymap.set("n", "<leader>gp", ":Gitsigns preview_hunk<CR>", {})
    end
  }
}
