Rails.application.routes.draw do
  root 'translate#index'

  resources :translate do
    collection do
      post :upload_file
    end
  end
end
