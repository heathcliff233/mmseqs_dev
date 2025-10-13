-- function HorizontalRule()
--   -- Replace the default rule with a proper Typst line command.
--   -- The '\\n' ensures it's on its own line, fixing wrapping issues.
--   return pandoc.RawBlock('typst', '#line(length: 100%)\\n')
-- end

-- Make long tables breakable across pages in Typst.
-- Pandoc's Typst writer wraps tables in a #figure(kind: table), which is kept intact
-- and can cause overflow/overlap on page breaks. We unwrap the figure and wrap the
-- inner table in a breakable block to allow page breaks inside the table.
-- Convert line breaks inside table cells to explicit Typst linebreaks so
-- multi-line content (e.g., items separated by <br>) actually wraps.
local function inline_breaks(el)
  if el.t == 'LineBreak' then
    return pandoc.RawInline('typst', '#linebreak()')
  end
  if el.t == 'SoftBreak' then
    -- Use a plain space for soft breaks to avoid concatenation.
    return pandoc.Str(' ')
  end
  if el.t == 'RawInline' and el.format and el.format:match('html') then
    local txt = el.text or ''
    if txt:match('^%s*<br%s*/?>%s*$') then
      return pandoc.RawInline('typst', '#linebreak()')
    end
  end
  return nil
end

function Table(tbl)
  -- Ensure breaks in table cells are preserved for Typst.
  local walked = pandoc.walk_block(tbl, { Inline = inline_breaks })
  local temp_doc = pandoc.Pandoc({walked})
  local t = pandoc.write(temp_doc, 'typst')

  -- Strip the outer figure wrapper while keeping inner alignment/table.
  -- Convert leading "#figure(" to nothing and remove trailing ", kind: table)".
  -- Be flexible about whitespace and newlines.
  t = t:gsub("^%s*#figure%(%s*", "")
  t = t:gsub(",%s*kind:%s*table%s*%)%s*$", "")

  -- If there's an outer align(center)[ ... ], remove it and keep the inner content.
  local inner = t:match("^%s*align%(%s*center%s*%)%s*%[(.*)%]%s*$")
  if inner then
    t = inner
  end

  -- Wrap the remaining #table(..) in a breakable block so it can split across pages.
  return pandoc.RawBlock('typst', '#block(breakable: true)[\n' .. t .. '\n]')
end
