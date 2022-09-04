function ide -d "Open a file/directory with intellij"
    set open "$argv[1]"
    if test -z "$open"
        set open '.'
    end
    nohup idea "$argv[1]" 2>/dev/null 1>/dev/null & disown
end
