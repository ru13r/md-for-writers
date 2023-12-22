-- fenced_block.lua
-- A "note" container environment

function Div(el)
    if el.classes[1] == "meta" then
      -- insert element in front
      if el.attributes.title then
        st = "\\begin{meta}{"..el.attributes.title.."}"
      else 
        st = "\\begin{meta}"
      end
      table.insert(
        el.content, 1,
        pandoc.RawBlock("latex", st))
      -- insert element at the back
      table.insert(
        el.content,
        pandoc.RawBlock("latex", "\\end{meta}"))
    end
    return el
  end