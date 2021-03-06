module CheatCode (..) where

import Char exposing (KeyCode)
import Dict exposing (Dict)
import Effects exposing (Effects, none)
import Set exposing (Set)
import String
import Task


type alias Model =
    { codeStatus : Dict String Int
    , mailbox : Signal.Mailbox String
    }


init : List String -> Signal.Mailbox String -> Model
init codes mailbox =
    { codeStatus = Dict.fromList <| List.map (\s -> ( s, 0 )) codes
    , mailbox = mailbox
    }


onlyShift : Set KeyCode -> Bool
onlyShift =
    Set.toList >> List.all ((==) 16)


soleMember : Set KeyCode -> Char -> Int -> Int
soleMember ks c prev =
    let
        k = Char.toCode c
    in
        case Set.size ks of
            0 ->
                prev

            _ ->
                let
                    accept = onlyShift (Set.remove k ks)
                in
                    if (Set.member k ks) then
                        if accept then
                            prev + 1
                        else
                            0
                    else
                        if accept then
                            prev
                        else
                            0


checkChar : Set KeyCode -> String -> Int -> Int
checkChar ks code matches =
    case String.uncons (String.dropLeft matches code) of
        Just ( next, _ ) ->
            soleMember ks next matches

        _ ->
            0


isComplete : ( String, Int ) -> Bool
isComplete ( s, n ) =
    String.length s == n


update : Set KeyCode -> Model -> ( Model, Effects String )
update ks model =
    let
        status =
            Dict.map (checkChar ks) model.codeStatus

        complete =
            List.head <| List.filter isComplete <| Dict.toList status
    in
        case complete of
            Nothing ->
                ( { model
                    | codeStatus = status
                  }
                , none
                )

            Just ( match, _ ) ->
                ( { model
                    | codeStatus = Dict.map (\_ _ -> 0) status
                  }
                , Signal.send model.mailbox.address match |> Task.map (\_ -> match) |> Effects.task
                )


mailbox : Signal.Mailbox String
mailbox =
    Signal.mailbox ""
